function main2(){
	var obj = JSON.parse('./data2.json');
	console.log(obj);
	document.querySelector("Headings").innerHTML = obj.Username; 
	console.log(obj.username);
}

document.addEventListener("DOMContentLoaded", main2());