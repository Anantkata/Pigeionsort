# Python program to implement Pigeonhole Sort */

# source code : "https://en.wikibooks.org/wiki/
# Algorithm_Implementation/Sorting/Pigeonhole_sort"
def pigeonhole_sort(a):
	# size of range of values in the list 
	# (ie, number of pigeonholes we need)
	my_min = min(a)
	my_max = max(a)
	size = my_max - my_min + 1

	# our list of pigeonholes
	holes = [0] * size

	# Populate the pigeonholes.
	for x in a:
		assert type(x) is int, "integers only please"
		holes[x - my_min] += 1

	# Put the elements back into the array in order.
	i = 0
	for count in range(size):
		while holes[count] > 0:
			holes[count] -= 1
			a[i] = count + my_min
			i += 1
			

a = [8, 3, 2, 7, 4, 6, 8]
print("Sorted order is : ", end = ' ')

pigeonhole_sort(a)
		
for i in range(0, len(a)):
	print(a[i], end = ' ')

<script>

// JavaScript program to implement
// Pigeonhole Sort

function pigeonhole_sort(arr, n)
{
	let min = arr[0];
	let max = arr[0];
	let range, i, j, index; 

	for(let a = 0; a < n; a++)
	{
		if(arr[a] > max)
			max = arr[a];
		if(arr[a] < min)
			min = arr[a];
	}

	range = max - min + 1;
	let phole = [];
	
	for(i = 0; i < n; i++)
	phole[i] = 0;

	for(i = 0; i < n; i++)
		phole[arr[i] - min]++;

	
	index = 0;

	for(j = 0; j < range; j++)
		while(phole[j] --> 0)
			arr[index++] = j + min;

}

// Driver Code

	let arr = [8, 3, 2, 7, 
				4, 6, 8];

	document.write("Sorted order is : ");

	pigeonhole_sort(arr,arr.length);
	
	for(let i = 0 ; i < arr.length ; i++)
		document.write(arr[i] + " ");
	
	// This code is contributed by target_2.
</script>

