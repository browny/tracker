
function run(keyword) {

	$.ajax({
		url: encodeURI('http://127.0.0.1:5000/parser/' + keyword),
		dataType: 'json',
		cache: false
	})
	.done(function(data) {
		console.dir(data);
		for (item in data['items']) {
			var title = data['items'][item]['title'];
			var link = data['items'][item]['link'];
			$('#result').append(
				'<li>' + title + '</li>' 
			);
			$('#result').append(
				jQuery('<a>').attr('href', link).attr('target','_blank').text(link)
			);
		}
	});
}


document.addEventListener('DOMContentLoaded', function() {
	console.log('doc ready!');

	$( "#target" ).submit(function( event ) {
		var keyword = $( "#keyword").val();
		run(keyword);
		event.preventDefault();
	});
});

