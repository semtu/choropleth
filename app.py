import flask
import numpy as np
import requests
import json
import pandas as pd
import plotly.express as px
from flask import Markup
import plotly.offline as po


app=flask.Flask(__name__,template_folder='templates')
@app.route('/', methods=['GET','POST'])
def main():

    if flask.request.method == 'GET':
        return flask.render_template('main.html')

    if flask.request.method == 'POST':
        if flask.request.form['gender_male'] == 'Male':
            gender_male=1
        else:
            gender_male=0
        if flask.request.form['may'] == 'Yes':
            may=1
        else:
            may=0
        if flask.request.form['march'] == 'Yes':
            march=1
        else:
            march=0
        if flask.request.form['august'] == 'Yes':
            august=1
        else:
            august=0
        if flask.request.form['september'] == 'Yes':
            september=1
        else:
            september=0
        if flask.request.form['june'] == 'Yes':
            june=1
        else:
            june=0
        if flask.request.form['february'] == 'Yes':
            february=1
        else:
            february=0
        if flask.request.form['october'] == 'Yes':
            october=1
        else:
            october=0
        if flask.request.form['november'] == 'Yes':
            november=1
        else:
            november=0
        if flask.request.form['july'] == 'Yes':
            july=1
        else:
            july=0
        if flask.request.form['december'] == 'Yes':
            december=1
        else:
            december=0
        if flask.request.form['april'] == 'Yes':
            april=1
        else:
            april=0
        if flask.request.form['january'] == 'Yes':
            january=1
        else:
            january=0
        age=flask.request.form['age']
        if flask.request.form['adult_group'] == 'Adult':
            adult_group=1
        else:
            adult_group=0
        if flask.request.form['NmA'] == 'Yes':
            NmA=1
        else:
            NmA=0
        if flask.request.form['NmC'] == 'Yes':
            NmC=1
        else:
            NmC=0
        if flask.request.form['NmW'] == 'Yes':
            NmW=1
        else:
            NmW=0
        if flask.request.form['alive'] == 'Alive':
            alive=1
        else:
            alive=0

        states=json.load(open('nigeria_geojson.geojson', 'r'))

        state_id_map={}
        for feature in states['features']:
            feature['id']=feature['properties']['cartodb_id']
            state_id_map[feature['properties']['state']]=feature['id']

        df=pd.DataFrame(data=['Niger','Borno','Taraba','Kaduna','Bauchi','Yobe','Zamfara','Adamawa','Kwara','Kebbi','Benue','Plateau','Kogi','Oyo','Nasarawa','Sokoto','Katsina','Jigawa','Cross River','Kano','Gombe','Edo','Delta','Ogun','Ondo','Rivers','Bayelsa','Osun','Fct, Abuja','Enugu','Akwa Ibom','Ekiti','Abia','Ebonyi','Imo','Anambra','Lagos'], columns=['State'])
        df['id']=df['State'].apply(lambda x: state_id_map[x])
        df=df[['id','State']]
        df['prediction']=df['id'].apply(lambda x: x==0)
        df['prediction']=df['prediction'].apply(lambda x: 1 if x=='False' else 0)
        df['prediction']=df['prediction'].astype(float)
        df['prediction'][[5,10,12,27,29,36,35,34,30]]=0.4
        df['prediction'][[6,8,9,11,13,14,17,22]]=0.53
        df['prediction'][[7,15,16,18,19,20]]=0.5147645473480225
        df['prediction'][[23,24,21,25,26,28,31,32,33]]=0.4862499237060547
        df['percent']=df['id'].apply(lambda x: x==0)
        df['percent']=df['percent'].apply(lambda x: 1 if x=='False' else 0)

        url1 = "https://www.plugai.xyz/inference/integer/eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiT2d1bl9SdXJhbF81MCJ9.XloM9ZumfC4MRCFZGWpPIl2hYKRPZJaB1LPxZeJKJ98"
        url2 = "https://www.plugai.xyz/inference/integer/eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiT2d1bl9VcmJhbl81MCJ9.8MtY4fu_i-qOKnnDVUwexfRhNPBdnrfpmXEKGBTLvMw"
        url3 = "https://www.plugai.xyz/inference/integer/eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiRkNUX1J1cmFsXzUwIn0.Y1frt_FtHu-cGb9GJodiB-Hl9nqFqKn0MQYyAY8y44k"
        url4 = "https://www.plugai.xyz/inference/integer/eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiRkNUX1VyYmFuXzUwIn0.yGnAmup5y2_PRbTQwLKSL_M0XH9MApEBaV4VAgwRjgc"
        url5 = "https://www.plugai.xyz/inference/integer/eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiS2FkdW5hX1J1cmFsXzUwIn0.BpTaJr8s-BblYLcEnRKDbfwy1olk3PBOQ8iCUkze26g"

        url_agg=[url1,url2,url3,url4,url5]
        response_agg=[]

        payload={'fig': ','.join([str(gender_male),str(may),str(march),str(august),str(september),str(june),str(february),str(october),str(november),str(july),str(december),str(april),str(january),str(age),str(adult_group),str(NmA),str(NmC),str(NmW),str(alive)])}

        files = [

        ]
        headers = {
        'Cookie': '__cfduid=dff1fabb883912efdce5fe0da9af16c871603217819'
        }

        for url in url_agg:
            response = requests.request("POST", url, headers=headers, data = payload, files = files)
            response_agg.append(response.text)

        test_prediction=[]
        idx2class={0: 'no', 1: 'a'}
        for i in range(0,5):
            model=response_agg[i].split('[[')[1].split(']]')[0]
            a=np.rint(float(model))
            #print(float(model))
            df['prediction'][i]=float(model)
            u,inv=np.unique(a,return_inverse=True)
            prediction=np.array([idx2class[x] for x in u])[inv].reshape(a.shape)
            if prediction=='no':
                percent=(float(model)/0.5)*100
                df['percent'][i]=np.rint(percent)
            else:
                percent=((1-float(model))/0.5)*100
                df['percent'][i]=np.rint(percent)
                test_prediction.append([percent,prediction,list(df['State'])[i]])
                for i in range(0,(len(test_prediction))):
                    percent_table=test_prediction[i][0]
                    print(percent_table)
            

            print(percent,prediction)
        length=len(test_prediction)
        df['predicted']=df['prediction'].round().astype(int)
        df['predicted']=df['predicted'].map({1: 'Yes', 0: 'No'})
        print(df)

        fig=px.choropleth(df,locations='id',geojson=states,color='prediction',hover_name='State',color_continuous_scale=px.colors.diverging.BrBG,color_continuous_midpoint=0.5,labels={'prediction_int':'prediction_int'})
        fig.update_geos(fitbounds="locations", visible=False) 
        #fig=fig.write_html("templates/plotly.html")
        fig_chart=po.plot(fig,output_type='div',include_plotlyjs=True)
        fig_chart1=Markup(fig_chart)

        choro2=px.choropleth_mapbox(df,locations='id',geojson=states,color='predicted',hover_name='State',mapbox_style='carto-positron',center={'lat':9.0820,'lon':8.6753},zoom=4,color_continuous_scale=[['No','green'],['Yes','red']],opacity=0.8,title='Locations of Meningitis in Nigeria')
        #choro2=choro2.write_html('templates/plotly2.html')
        choro_chart=po.plot(choro2,output_type='div',include_plotlyjs=True)
        choro_chart1=Markup(choro_chart)
        return flask.render_template('main.html',percent=percent,result=prediction,fig_chart2=fig_chart1,choro_chart2=choro_chart1,test_prediction=sorted(test_prediction),length=length)

@app.route('/map1/')
def plotly():
    return flask.render_template('plotly.html')

@app.route('/map2/')
def plotly2():
    return flask.render_template('plotly2.html')

if __name__=='__main__':
    app.run()
