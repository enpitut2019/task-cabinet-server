import json
import random
import collections as cl
import datetime
from faker import Factory

def task():
    jst = datetime.timezone(datetime.timedelta(hours=+9), 'JST')
    fake = Factory.create('ja_JP')
    ys = []  # json書き込み用配列
    for i in range(10):
        date = datetime.datetime.now(jst).strftime("%Y-%m-%d %H:%M:%S")  # created_at & updated_at用
        fields = cl.OrderedDict()  # 格納するフィールドを定義
        fields["name"] = fake.name()
        fields["state"] = random.randint(0, 1)
        fields["dead_line"] = fake.date_time_this_decade(before_now=False, after_now=True, tzinfo=None).strftime("%Y-%m-%d %H:%M:%S")
        fields["created_at"] = date
        fields["updated_at"] = date
        data = cl.OrderedDict()
        data["model"] = "task_cabinet.task"  # 対象のmodelを設定
        data["pk"] = i + 1  # PrimaryKeyを設定
        data["fields"] = fields  # 格納するフィールドを設定
        ys.append(data)  # json書き込み用配列に追加
    fw = open('components/faker_task.json', 'w')
    json.dump(ys, fw, indent=2, ensure_ascii=False)  # 中間fixtureファイルを出力


if __name__ == '__main__':
    task()
