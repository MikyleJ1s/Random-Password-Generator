function button_logic() {
    var use_length = document.forms["user_inputs"]["use_length"].value;
    if (use_length == "" || use_length == null) { 
             document.getElementById('generate_button').disabled = true; 
               return true;
         } else { 
             document.getElementById('generate_button').disabled = false;
             return false;
         }  
};

