# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_python38_app]
# [START gae_python3_app]
import datetime, sys

from flask import Flask, render_template, request
from google.cloud import automl_v1
from google.api_core.client_options import ClientOptions

# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)

def get_prediction(input, model_name):
  options = ClientOptions(api_endpoint='automl.googleapis.com')
  prediction_client = automl_v1.PredictionServiceClient(client_options=options)


  payload = {'text_snippet': {'content': input, 'mime_type': 'text/plain'} }
  params = {}
  automl_request = automl_v1.PredictRequest(name=model_name, payload=payload, params=params)
  
  automl_response = prediction_client.predict(automl_request)

  return automl_response  # waits until request is returned

@app.route('/', methods=['GET','POST'])
def root():
    form_data = ""
    difficulty = ""
    if request.method == 'POST':
        form_data = request.form.get('textinput')
        difficulty = get_prediction(form_data, "projects/79067930854/locations/us-central1/models/TCN377099502978334720").payload[0].display_name
        result = "Your text is labelled as " + difficulty
    return render_template('index.html', result=result, text=form_data)

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python3_app]
# [END gae_python38_app]