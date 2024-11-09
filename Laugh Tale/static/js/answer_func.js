//Functions 

// You can access the Flask variable `titles` here by embedding it into the JavaScript code
var title_answer = "{{ titles[0] }}";
    
function answer(anime_name) {
    document.getElementById("enter_anime").value = title_answer;
}

