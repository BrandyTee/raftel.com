{% extends 'raftel base.html' %}

{% block raftel %}



<!-- <script src = " {{ url_for('static', filename= 'js/answer_func.js' ) }}" ></script> -->




<body>
<center>

<h2 id="use" > Guess The Anime </h2>

<div id="alert" class="alert alert-secondary" role="alert">
 Guess the anime
</div>


<div class="card">
      <img id="anime_image" src="{{ images[0] }}" class="d-block w-100" alt="..." width="450" height="320">
</div>
    


<br>
<br>


<div>
<form method="POST" action = "" class="d-flex" role="search" >
{{ form.hidden_tag() }}
    <input class="form-control dark" type="search" id="enter_anime" placeholder="Enter Anime" aria-label="enter_name" name="anime" autocomplete="off">
    <br/>
    <br/>
</div>          


<div class="btn-group" role="group" aria-label="Basic mixed styles example">
  <button type="button" class="btn btn-secondary" onclick="hint()">Hint</button>
  <button type="button" class="btn btn-secondary" onclick="answer()">Answer</button>
</div>



<br>
<br>
<button type="button" class="btn btn-success" onclick="enter()">SUBMIT</button>

</center>

<script type="text/javascript">

    let length = "{{ length }}";
    
    // You can access the Flask variable `titles` here by embedding it into the JavaScript code
        
    var user_answer = document.getElementById("enter_anime");
        
        
    let images = {{ images | tojson }};
    let number = 0;    
    //var image = {{ images }};
    var titles = {{ titles | tojson }};
        
    //let image_answer = images[number];
    var title_answer = titles[number];
    var anime_image = document.getElementById("anime_image");
    var alerts = document.getElementById("alert");
    var hints = 1;
    
    function hint() {
        
        let hint_answer = user_answer.value = titles[number][0];
        //hint_answer = hint_answer + hints
        
        user_answer.value += titles[number][1];
        //hints = (hints + 1) % titles.length;
        user_answer.value += titles[number][2];
        
        
        
        
}
    
    
    function answer() {
        
        document.getElementById("enter_anime").value = titles[number];
        number = (number + 1) % titles.length;
        
        
}

    function enter() {
    
        //Run conditionals
        if (user_answer.value.trim() !== title_answer){
            
            user_answer.value = "";
            user_answer.placeholder = "Enter Anime";
            
        }
         else     
        {
            //var number = 1;
            number = (number + 1) % images.length;
            let image_answer = images[number];
            document.getElementById("anime_image").src =  image_answer;
            title_answer = titles[number];
            
            
            user_answer.value = "";
            user_answer.placeholder = "Enter Anime";
        
            
            } 
    
    
}

</script>

</body>


{% endblock %}