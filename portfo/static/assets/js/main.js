(function($) {

	document.getElementById("contact-form").addEventListener("submit", function(event) {
		event.preventDefault(); // Prevent form submission
	  
		// Show thank you message and hide the form
		document.getElementById("form-container").style.display = "none";
		document.getElementById("thank-you-message").style.display = "block";
	  });
	
	const elButton = document.querySelector('.chocolate-button');

	elButton.addEventListener('mousedown', (event) => {
	if (!elButton.matches(':focus')) { 
		elButton.style.setProperty('--x', event.offsetX);
		elButton.style.setProperty('--y', event.offsetY);
	}
	});

	var	$window = $(window),
		$body = $('body'),
		$nav = $('#nav');

	// Breakpoints.
		breakpoints({
			xlarge:  [ '1281px',  '1680px' ],
			large:   [ '981px',   '1280px' ],
			medium:  [ '737px',   '980px'  ],
			small:   [ null,      '736px'  ]
		});

	// Play initial animations on page load.
		$window.on('load', function() {
			window.setTimeout(function() {
				$body.removeClass('is-preload');
			}, 100);
		});

	// Scrolly.
		$('#nav a, .scrolly').scrolly({
			speed: 1000,
			offset: function() { return $nav.height(); }
		});

})(jQuery);