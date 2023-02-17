from flask import Flask, render_template, url_for
import pickle
import pandas

popular_df=pickle.load(open('popular.pkl', 'rb'))

app = Flask (__name__) 

@app.route('/')
def index ():
    return render_template("index.html",
                          book_name=list(popular_df['Book-Title'].values),
                          author=list(popular_df['Book-Author'].values),
                          image=list(popular_df['Image-URL-M'].values),
                          votes=list(popular_df['no_of_rating'].values),
                          rating=list(popular_df['avg_rating'].values),
                          )

    if  __name__ == "__main__" :
      app.run(debug =True)
