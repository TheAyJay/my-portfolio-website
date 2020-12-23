$(document).ready(function(){

    var numberOfCards = $('.collapsed').length;

    $('.collapsed').click(function(){

        // Get the div id of the particular item that was clicked (e.g. "show-details-text1")
        var targetElement = $(this).attr('id');
        // Get the number in the sequence for that attribute (e.g. 1 from "show-details-text1")
        var targetElementNumber = targetElement.substring((targetElement.length - 1), targetElement.length);
        // Get the overarching set of target elements (e.g. "show-details-text" from "show-details-text1")
        var targetElementSet = targetElement.substring(0, (targetElement.length - 1));
        // Get the current text of that element (e.g. "Show More")
        var text = $('#'+targetElement).text();

        // If the text is set to "Show More", then set all elements to "Show More" and the one that was
        // clicked to "Show Less"
        if (text == 'Show More')
        {
            var i;
            for (i = 1; i <= numberOfCards; i++)
            {
                $('#' + targetElementSet + i).text('Show More');
            }
            $('#' + targetElement).text('Show Less');
        }
        // If the text is set to "Show Less", then set all elements to "Show More" (the default)
        else
        {
            var i;
            for (i = 1; i <= numberOfCards; i++)
            {
                $('#' + targetElementSet + i).text('Show More');
            }
        }
    });

});