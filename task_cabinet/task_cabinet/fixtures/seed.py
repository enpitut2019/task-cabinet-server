import django
import makefixture
import json

if __name__ == '__main__':
    # fixtureファイルを作成する
    # ここでできたfixtureファイルをDBに反映させるには'python manage.py loaddata seed'を実行する
    makefixture.task()  # 各modelのfixtureファイルを作成

    component_data = []  # 各fixtureファイルのjsonを格納するためのリスト
    master_data = []  # 各fixtureファイルを結合したデータを格納するためのリスト
    src = ["components/faker_task.json",]
    for i in range(len(src)):
        fr = open(src[i], 'r')
        component_data = json.load(fr)
        master_data.extend(component_data)  # 各fixtureデータを結合
    fw = open('seed.json', 'w')
    json.dump(master_data, fw, indent=2, ensure_ascii=False)  # 結合したfixtureファイルを出力
