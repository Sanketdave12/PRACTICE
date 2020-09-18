def get_data(place,key):
    url = f"https://maps.googleapis.com/maps/api/place/textsearch/json?query={place}&key={key}"
    page = requests.get(url)
    try:
        if page.status_code == 200:
            data = page.json()
            place_add = data['results'][0]['formatted_address']
            place_name = data['results'][0]['name']
            place_id = data['results'][0]['place_id']
            photo_ref = data['results'][0]['photos'][0]['photo_reference']
            print('place_add --> ',place_add)
            print('place name --> ',place_name)
            #print('place id --> ',place_id)
            #print('photo ref --> ',photo_ref)
            photo = f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference={photo_ref}&key={key}"
            req = requests.get(photo)
            if req.status_code == 200:
                with open('image.jpg','wb') as fp:
                    fp.write(req.content)
                    fp.close()
                plt.imshow(plt.imread('image.jpg'))
                plt.title(place_name,fontsize=20)
                plt.xlabel(place_add,fontsize=20)
                plt.xticks([])
                plt.yticks([])
                plt.show()
            else:
                print('image not found')
        else:
             print('error.....!!!! somthing went wrong')
    except Exception as e:
        print('Errorr----> ',e)
       

if __name__ == '__main__':
    import requests
    import json 
    import matplotlib.pyplot as plt
    key = "AIzaSyCNmQqNQd9xJKHTPtdoAnBi1LWxiJ96wUo"
    place = input('enter a place to search : ').replace(' ','%20').lower()
    get_data(place,key)
