import json


def read_json(json_file_path: str):
    with open(json_file_path, 'r') as f:
        return json.load(f)


def process_annotation(anno_file_path: str):
    data = read_json(json_file_path=anno_file_path)
    annotations = data['dcu_format']['annotations']
    for anno in annotations:
        if anno['category'] == 'text':
            img_uid, value = anno['image_uid'], anno['value']
            with open('label.txt', 'a') as f:
                f.write(f'{img_uid}, {value}\n')


if __name__ == '__main__':
    file_path = 'anno.json'
    process_annotation(anno_file_path=file_path)