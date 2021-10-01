import numpy as np

nan = np.nan # not a number đại diện cho các sản phẩm chưa được đánh giá
ratings_matrix = np.array([[2.0, 3.0, 4.0, 1.0, 3.0, 1.0, 1.0, 2.0, 2.0, 1.0, 4.0, 1.0, 1.0, 2.0, 1.0, 3.0, 1.0, 3.0, -1.0, -1.0], [3.0, 3.0, 1.0, 1.0, 1.0, 2.0, 1.0, 1.0, 1.0, 3.0, 2.0, 3.0, 2.0, 3.0, 4.0, 4.0, 1.0, 2.0, -1.0, -1.0], [1.0, 4.0, 1.0, 1.0, 1.0, 1.0, 1.0, 2.0, 1.0, 2.0, 2.0, 1.0, 2.0, 3.0, 3.0, 4.0, 3.0, 4.0, -1.0, -1.0], [1.0, 1.0, 2.0, 3.0, 1.0, 4.0, 1.0, 3.0, 4.0, 3.0, 4.0, 2.0, 2.0, 2.0, 1.0, 2.0, 1.0, 2.0, -1.0, -1.0], [1.0, 3.0, 4.0, 4.0, 1.0, 1.0, 1.0, 
3.0, 3.0, 3.0, 3.0, 4.0, 4.0, 4.0, 2.0, 3.0, 3.0, 2.0, -1.0, -1.0], [4.0, 2.0, 2.0, 3.0, 1.0, 4.0, 1.0, 3.0, 4.0, 4.0, 1.0, 3.0, 3.0, 1.0, 4.0, 1.0, 2.0, 2.0, -1.0, -1.0], [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0], [1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, 
-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0], [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0], [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0], [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, 
-1.0, -1.0, -1.0, -1.0, -1.0, -1.0], [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0], [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0], [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, 
-1.0, -1.0, -1.0, -1.0, -1.0], [1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0], [1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0], [1.0, 
-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]])

# indices for vector
def specified_rating_indices(u):
    return list(map(tuple, np.where(np.isfinite(u))))

def mean(u):
    # may use specified_rating_indices but use more time
    specified_ratings = u[specified_rating_indices(u)]#u[np.isfinite(u)]


    m = sum(specified_ratings)/np.shape(specified_ratings)[0]

    return m

def all_user_mean_ratings(ratings_matrix):
    return np.array([mean(ratings_matrix[u, :]) for u in range(ratings_matrix.shape[0])])

def get_mean_centered_ratings_matrix(ratings_matrix):
    users_mean_rating = all_user_mean_ratings(ratings_matrix)
    mean_centered_ratings_matrix = ratings_matrix - np.reshape(users_mean_rating, [-1, 1])
  
  
    return mean_centered_ratings_matrix


# array([[ 1.5,  0.5,  1.5, -1.5, -0.5, -1.5],
#          [ 1.2,  2.2,  nan, -0.8, -1.8, -0.8],
#          [ nan,  1. ,  1. , -1. , -1. ,  nan],
#          [-1.5, -0.5, -0.5,  0.5,  0.5,  1.5],
#          [-1. ,  nan, -1. ,  0. ,  1. ,  1. ]])

def pearson(u, v):
    mean_u = mean(u)
    mean_v = mean(v)
    
    specified_rating_indices_u = set(specified_rating_indices(u)[0])
    specified_rating_indices_v = set(specified_rating_indices(v)[0])
    
    mutually_specified_ratings_indices = specified_rating_indices_u.intersection(specified_rating_indices_v)
    mutually_specified_ratings_indices = list(mutually_specified_ratings_indices)
    
    u_mutually = u[mutually_specified_ratings_indices]
    v_mutually = v[mutually_specified_ratings_indices]
      
    centralized_mutually_u = u_mutually - mean_u
    centralized_mutually_v = v_mutually - mean_v

    result = np.sum(np.multiply(centralized_mutually_u, centralized_mutually_v)) 
    result = result / (np.sqrt(np.sum(np.square(centralized_mutually_u))) * np.sqrt(np.sum(np.square(centralized_mutually_v))))
    if np.isnan(result) :
        return 0
    return result

def get_user_similarity_value_for(u_index, ratings_matrix):
    user_ratings = ratings_matrix[u_index, :]
    similarity_value = np.array([pearson(ratings_matrix[i, :], user_ratings) for i in range(ratings_matrix.shape[0])])
    return similarity_value

def get_user_similarity_matrix(ratings_matrix):
    similarity_matrix = []
    for u_index in range(ratings_matrix.shape[0]):
        similarity_value = get_user_similarity_value_for(u_index, ratings_matrix)
        similarity_matrix.append(similarity_value)
    return np.array(similarity_matrix)




def predict(u_index, i_index, k,ratings_matrix):
# k là số lượng người dùng giống với người dùng cần dự đoán
# ta có thể tùy chọn giá trị k này
    user_similarity_matrix = get_user_similarity_matrix(ratings_matrix) 
    mean_centered_ratings_matrix = get_mean_centered_ratings_matrix(ratings_matrix)
    users_mean_rating = all_user_mean_ratings(ratings_matrix)
 
    similarity_value = user_similarity_matrix[u_index]
    sorted_users_similar = np.argsort(similarity_value)
    sorted_users_similar = np.flip(sorted_users_similar, axis=0)
        
    users_rated_item = specified_rating_indices(ratings_matrix[:, i_index])[0]
    
    ranked_similar_user_rated_item = [u for u in sorted_users_similar if u in users_rated_item]
    
    if k < len(ranked_similar_user_rated_item):
        top_k_similar_user = ranked_similar_user_rated_item[0:k]   
    else:
        top_k_similar_user = np.array(ranked_similar_user_rated_item)
            
    ratings_in_item = mean_centered_ratings_matrix[:, i_index]
    top_k_ratings = ratings_in_item[top_k_similar_user]
    
    top_k_similarity_value = similarity_value[top_k_similar_user]
    
    r_hat = users_mean_rating[u_index] + np.sum(top_k_ratings * top_k_similarity_value)/np.sum(np.abs(top_k_similarity_value))
    return r_hat

def predict_top_k_items_of_user(u_index, k_users,ratings_matrix):
    items = []
    # print("ratings_matrix.shape[1]",ratings_matrix.shape[1])
    for i_index in range(ratings_matrix.shape[1]):
       # if np.isnan(ratings_matrix[u_index][i_index]):
        rating = predict(u_index, i_index, k_users,ratings_matrix)
        items.append((i_index, rating))
    
    items = sorted(items, key=lambda tup: tup[1])

    return list(reversed(items))



if __name__ == '__main__':
    # print("ma trận hiệu")
    # print(mean_centered_ratings_matrix)
    # print("ma trận vector")
    # print(user_similarity_matrix)
    
    print(predict_top_k_items_of_user(2,2,ratings_matrix))

