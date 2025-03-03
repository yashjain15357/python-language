# Copy VS view
import numpy as np 
arr= np.array([[1,2,3,4,5],[12,34,34,35,45]])
# copy:-Any changes made to the copy will not affect original array , change in the array will not affecte the copy array
copy_arr= np.copy(arr)
copy_arr1 = arr.copy()
arr[1][0]=0
copy_arr[1][0]=10
# print(arr)
# print(copy_arr)
# print(copy_arr1)

# View :-Any changes made to the view will affect the original array, and any changes made to the original array will affect the view.

arr= np.array([[1,2,3,4,5],[12,34,34,35,45]])
# copy:-Any changes made to the copy will not affect original array , change in the array not affecte the copy array
# view_arr= np.view(arr) #// this is wrong syntax of the view
view_arr1 = arr.view()
arr[1][0]=0
# view_arr[1][0]=10
# print(view_arr)
print(arr)
print(view_arr1) 
# np.view 