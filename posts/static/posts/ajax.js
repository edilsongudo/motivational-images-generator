$(document).ready(function() {

    function getvalues() {
        var csrfToken = $('input[name="csrfmiddlewaretoken"]').val()
        var primary_text_color = $('input[name="primary_text_color"]').val()
        var primary_font_type = $('select[name="primary_font_type"]').val()
        var primary_font_size = $('input[name="primary_font_size"]').val()
        var brand_name = $('input[name="brand_name"]').val()
        var brand_name_font_type = $('select[name="brand_name_font_type"]').val()
        var brand_name_font_size = $('input[name="brand_name_font_size"]').val()
        var brand_name_font_color = $('input[name="brand_name_font_color"]').val()
        var line_separation = $('input[name="line_separation"]').val()
        var logo_size = $('input[name="logo_size"]').val()
        var brightness = $('input[name="brightness"]').val()
        var greyscale = $('input[name="greyscale"]').val()
        // var logo_path = $('label[for="id_logo_path"]').val()

        var dict = {"primary_text_color": primary_text_color,
                    "primary_font_type": primary_font_type, "primary_font_size": primary_font_size,
                    "brand_name": brand_name, "brand_name_font_type": brand_name_font_type,
                    "brand_name_font_size": brand_name_font_size, "brand_name_font_color": brand_name_font_color,
                    "logo_size": logo_size, "brightness": brightness, "greyscale": greyscale,
                    "line_separation": line_separation
                    }

        var json = JSON.stringify(dict)
        console.log(json)

         $.ajax({
            url: '',
            headers: {'X-CSRFToken': csrfToken},
            dataType: 'json',
            data: json,
            type: 'post',
            success: function(response) {
                $('.preview-image').attr('src', '../../../media/images/temp/preview/' + response.response)
                console.log('Response: ', response)
            }
        })

    }
    $('form').change(getvalues)

});

