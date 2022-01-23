$(document).ready(()=>{

function generateOutput(value){
	if(value===true)
	return `
	<div class="alert alert-success alert-dismissible">
	  <button type="button" class="close" data-dismiss="alert">&times;</button>
	    Team2 will win it
	</div>
	`

	else{
	return `
	<div class="alert alert-success alert-dismissible">
	  <button type="button" class="close" data-dismiss="alert">&times;</button>
	    Team1 will win it
	</div>
	`
	}
}

$('#submit').click((e)=>{
	e.preventDefault();
	var innings1_runs=$('#innings1_runs').val()
	var innings1_wickets=$('#innings1_wickets').val()
	var innings1_overs_batted=$('#innings1_overs_batted').val()
	var algo = $('#algo').val()
	$.getJSON(`/predict?innings1_runs=${innings1_runs}&innings1_wickets=${innings1_wickets}&innings1_overs_batted=${innings1_overs_batted}&algo=${algo}`, function(result){

		$("#output").html(generateOutput(result.prediction))
    });

})

})