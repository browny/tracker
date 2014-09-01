
function run(keyword) {

	$.ajax({
		url: 'http://127.0.0.1:5000/parser/' + keyword,
		dataType: 'json',
		success: function(data) {
			console.dir(data);
			for (item in data['items']) {
				$('#result').append(
					'<li>' + data['items'][item]['title'] + '</li>');
			}
		}
	});
}


document.addEventListener('DOMContentLoaded', function() {
  console.log('doc ready!');
  run('htc');
});
