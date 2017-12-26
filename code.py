import web

# render a template;
render = web.template.render('templates/')
# url pattern; each url to a solution.
urls = (
    '/', 'index',
    '/movie/(\d+)','movie',
    '/cast/(.*)', 'cast',
)
# test without database
#
# movies = [
#     {
#         'title': 'Forrest Gump',
#         'year': 1994,
#     },
#     {
#         'title': 'Titanic',
#         'year': 1997,
#     }
# ]

# connect to database, db is database object;
db = web.database(dbn='sqlite', db='MovieSite.db')
# solution to index page;
class index:
    # when someone raises a GET request, use this function;
    # esp, viist this site;
    def GET(self):
        # test without database
        #
        # page = ''
        # for m in movies:
        #     #page += '%s(%d)\n'%(m['title'], m['year'])
        #     page += '%s (%d)\n' % (m['title'], m['year'])
        # return page

        # select a table, movies is a table object;
        movies = db.select('movie')
        # render index page with movies object; look up in index.html(details of renderation);
        return render.index(movies)
    # when someone raises a POST request, use this function;
    # esp, post a form to the server;
    def POST(self):
        # web.input() receive parameters from the POST request;
        # eg: when searching, post the value in the "input" tag;
        data = web.input()
        # r'%' 防止python对%的转义; %content%表示content前后匹配任意多字符;
        condition = r'title like "%' + data.title + r'%"'
        movies = db.select('movie', where=condition)
        return render.index(movies)

# solution to movie page;
class movie:
    # when visit with parameter;
    # eg: movie/123456
    def GET(self, movie_id):
        movie_id = int(movie_id)
        # still unclear with vars = locals()[0]
        movie = db.select('movie', where='id=$movie_id', vars=locals() )[0]
        casts_list = movie.casts.split(',')
        casts = []
        for cast in casts_list:
            casts.append(cast)
        return render.movie(movie, casts)


class cast:
    def GET(self, cast_name):
        # condition = r'casts like "%' + cast_name + r'%"'
        condition = r'casts like "%' + cast_name + r'%"'
        # condition = r'origin like "%' + cast_name + r'%"'
        movies = db.select('movie', where=condition)
        return render.index(movies)



# not so clear with it
if __name__ == "__main__":
    app = web.application(urls, globals() )
    app.run()
