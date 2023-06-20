class TravelBlog:
    total_blogs = 0


tb1 = TravelBlog()
tb1.name = 'Франция'
setattr(tb1, 'days', 6)

TravelBlog.total_blogs += 1

tb2 = TravelBlog()
setattr(tb2, 'name', 'Италия')
tb2.days = 5

setattr(TravelBlog, 'total_blogs', 2)
