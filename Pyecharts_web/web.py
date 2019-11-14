from pyecharts.charts import Radar
from pyecharts import options as opts
from flask import Flask,render_template
import pymysql

app = Flask(__name__,static_folder='templates')

# db = pymysql.connect(
#         host='127.0.0.1',
#         user='root',
#         passwd='123456',
#         port=3306,
#         db = 'web',
#         charset='utf8',
# )
# cd=db.cursor()
# sql = 'SELECT title,value FROM cs'
# cd.execute(sql)
# data = cd.fetchall()
# v1 = []
# v2 = []
# for i in data:
#     v1.append(i[0])
#     v2.append(i[1])

v1 = ['data','data2','data3','data4']
v2 = [60,80,90,100]

def radar():
    r = (
        Radar()
        .add_schema(schema=(
            opts.RadarIndicatorItem(v1[0],max_=v2[0]),
            opts.RadarIndicatorItem(v1[1],max_=v2[1]),
            opts.RadarIndicatorItem(v1[2], max_=v2[2]),
            opts.RadarIndicatorItem(v1[3], max_=v2[3]),
        ))
        .add('物联网可视化',[v2])
        .set_global_opts(opts.TitleOpts(title='大数据比赛可视化项目'))
    )
    return r

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/radarchar')
def get_radar_char():
    r = radar()
    return r.dump_options_with_quotes()

if __name__ == '__main__':
    app.run()