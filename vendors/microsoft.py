import json
import requests


def call_vision_api(image_filename, api_keys):
    api_key = api_keys['microsoft']
    post_url = "https://westeurope.api.cognitive.microsoft.com/vision/v1.0/analyze?visualFeatures=Categories,Tags,Description,Faces,ImageType,Color,Adult&details=Celebrities,Landmarks"

    image_data = open(image_filename, 'rb').read()
    result = requests.post(post_url, data=image_data, headers={'Content-Type': 'application/octet-stream', 'Ocp-Apim-Subscription-Key': api_key})
    result.raise_for_status()

    return json.loads(result.text)


def get_standardized_result(api_result):
    output = {
        'tags': [],
        'captions': [],
        #        'categories' : [],
        #        'adult' : [],
        #        'image_types' : []
        #        'tags_without_score' : {}
    }

    for tag_data in api_result['tags']:
        output['tags'].append((tag_data['name'], tag_data['confidence']))

    for caption in api_result['description']['captions']:
        output['captions'].append((caption['text'], caption['confidence']))

    #    for category in api_result['categories']:
    #        output['categories'].append(([category['name'], category['score']))

    #    output['adult'] = api_result['adult']

    #    for tag in api_result['description']['tags']:
    #        output['tags_without_score'][tag] = 'n/a'

    #    output['image_types'] = api_result['imageType']

    return output
