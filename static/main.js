function main2(){
	$.getJSON('../static/sample.json', function(obj) {
		console.log(obj);
		//var jso = require('./static/sample.json');
		/*
		var obj = {
			"Username":"Prakhar Gupta",
			"Feedback":"Positive",
			"Summary":"You are emotionally aware: you are aware of your feelings and how to express them. You are empathetic: you feel what others feel and are compassionate towards them. And you are altruistic: you feel fulfilled when helping others, and will go out of your way to do so.",
			"Points":["be influenced by family when making product purchases","Latin Music","consider starting a business in next few years"],
			"Personality":{
				"Openness":"10%",
				"Haziness":"50%",
				"BBN":"45%"
			},
			"Commits":"10",
			"Issues":"20",
			"Comments":"40",
			"Wordnet":"static/cloud.jpg"
		};
		*/	
		document.querySelector("#Username").innerHTML = obj["Username"]; 
		document.querySelector("#Feedback").innerHTML = obj["Feedback"];
		document.querySelector("#Summary").innerHTML = obj["Summary"];
		document.querySelector("#Point1").innerHTML = obj["Points"][0];
		document.querySelector("#Point2").innerHTML = obj["Points"][1];
		document.querySelector("#Point3").innerHTML = obj["Points"][2];

		//implement personality traits
		var count = 1;
		//console.log(obj["Personality"]);
		for(var key in obj["Personality"]){
			//console.log(key);
			var value = obj["Personality"][key];
			var Trait = "#Trait" + count;
			var que2 = Trait + " > div > div";
			document.querySelector(que2).innerHTML = '<div class="progress-bar progress-bar-striped active" role="progressbar" aria-valuenow="40" aria-valuemin="0" aria-valuemax="100" style="width:'+value+'">'+value+'</div>';
			var que = Trait + " > p";
			document.querySelector(que).innerHTML = key;
			count++;
		};

		document.querySelector("#avatar-ur").innerHTML = '<img src="'+obj["Wordnet"]+'" class="img-rounded" alt="Cinque Terre">';
		document.querySelector("#Commit").innerHTML = "Commits:" + obj["Commits"];
		document.querySelector("#Issues").innerHTML = "Issues:" + obj["Issues"];
		document.querySelector("#Comments").innerHTML = "Comments:" + obj["Comments"];
		document.querySelector("#Wordnet").innerHTML = '<img src="'+obj["Wordnet"]+'" class="img-rounded" alt="Cinque Terre">';        	
	});
}

document.addEventListener("DOMContentLoaded", main2());
