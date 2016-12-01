def merge_sort(arr):
	if len(arr)>1:
		mid=len(arr)//2
		left=arr[:mid]
		right=arr[mid:]
		
		merge_sort(left)
		merge_sort(right)
		
		i=0
		j=0
		k=0
		while i<len(left) and j<len(right):
			if left[i]<=right[j]:
				arr[k]=left[i]
				k+=1
				i+=1
			else:
				arr[k]=right[j]
				k+=1
				j+=1
		while i<len(left):
			arr[k]=left[i]
			i+=1
			k+=1
		while j<len(right):
			arr[k]=right[j]
			k+=1
			j+=1
arr=[56,20,16,86,3,45,7,19,36,3,45]
merge_sort(arr)
print(arr)
		
