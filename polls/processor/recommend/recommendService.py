from polls.models import Comment, User,Product
import numpy as np

nan = np.nan
def get_list_id_user() :
    id_users = User.objects.values_list('id', flat=True)
    return id_users.all()

def get_list_id_item() :
    id_items = Product.objects.values_list('id', flat=True)
  
    return id_items.all()

def find_id_item_from_index(index):
    id_items = get_list_id_item()
    for i, item in enumerate(id_items):
        if i==index :
            return item
    return -1

def find_index_from_iduser(id_user) :
    id_users = get_list_id_user()
    for index, item in enumerate(id_users):
        if item==id_user :
            return index
    return -1

def find_rate_by_iduser_and_iditem(idser,id_item) :
    objects = Comment.objects.filter(
        iduser=idser,idproduct = id_item
        ).values('rate')
    if(objects):
        print('bình luân của sản phẩm :',objects[0]['rate'])
        return objects[0]['rate']
    return -1


def find_id_user_from_index(index):
    id_users = get_list_id_user()
    for i, item in enumerate(id_users):
    
        if i==index :
            return item
    return -1

def get_list_item_recomment_for_user(list_datas):
    resultRecommend  = []
  
    if len(list_datas) == 0 :
        return resultRecommend

    for item in range(len(list_datas)) :
       
        index_item = list_datas[item][0]
        value_rating = list_datas[item][1]
  
        if np.isnan(value_rating) == False :
            id_item  = find_id_item_from_index(index_item)
          
            item = Product.objects.get(id=id_item) 
            resultRecommend.append(item)
    return resultRecommend

def makeRatingMatrix():
    
    total_user  = User.objects.count()
    total_item = Product.objects.count()
    zeors_array = np.zeros( (total_user, total_item) )

    for x in range(total_user):
        for y in range(total_item):
            id_user=find_id_user_from_index(x)
            id_item = find_id_item_from_index(y)
            rating = find_rate_by_iduser_and_iditem(id_user,id_item)
            zeors_array[x][y] = rating
            
    ratings_matrix = np.array(zeors_array.tolist())
    return ratings_matrix

if __name__ == '__main__':
    print(makeRatingMatrix())
    