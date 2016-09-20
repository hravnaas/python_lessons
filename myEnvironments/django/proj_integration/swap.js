function rotate(arr, val)
{
	for(var i = 0; i < arr.length; i++)
	{
		console.log(arr)
		var moveIndex = getNewindex(i, val, arr.length);
		temp = arr[moveIndex];
		arr[moveIndex] = arr[i];
		arr[i] = temp;
	}
}

function getNewindex(i, val, length)
{
	x = i + val;
	if(x > length - 1)
		return length - x;
	return x;
}

// Test it
var arr = [1, 3, 5, 8];
rotate(arr, 2);
if(arr === [5, 8, 1, 3])
  console.log("Passsed test 1");
else
{
  console.log("Failed test 1");
  console.log(arr)
}
