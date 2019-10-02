var datas = "";

$('#get').click(function() { //get here is the id of the button targetted
    console.log('working');
    $.ajax({ 
        // The URL for the request
        url: "http://127.0.0.1:8000/ordercreatestatus/",      
        // Whether this is a POST or GET request
        type: "GET",
        // The type of data we expect back
        dataType : "json",
    })
      // Code to run if the request succeeds (is done);
      // The response is passed to the function
      .done(function( datas ) {
        $('h1').text( datas[3].order_ids );
        //  $( "<h1>" ).text( json.title ).appendTo( "body" );
        //  $( "<div class=\"content\">").html( json.html ).appendTo( "body" );
        console.log(datas);
      });
});

$("#post").click(function(){
  $.ajax({
    type:"POST",
    url:"http://127.0.0.1:8000/ordercreatestatus/",
    //dataType: "json",
    //contentType: "application/json; charset=utf-8",
    data: {
        "order_ids":"AB45685625412521",
        "ser_no":"http://127.0.0.1:8000/seriallist/1/"
     },
     //processData: true, 
     success: function(response) {          
        console.log(response);
      }  
  });
});

//below post request block is for sending post request using simple post function in jquery only
/*$("#post").click(function(){
  $.post("http://127.0.0.1:8000/programmers/",
  {
    name: "Donald Duck",
    languages: "http://127.0.0.1:8000/languages/5/"
  },
  function(data, status){
    alert("Data: " + data + "\nStatus: " + status);
  });
}); 
*/
