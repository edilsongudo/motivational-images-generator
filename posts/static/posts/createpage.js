$(document).ready(function() {


        $('#generate').click(
                function(e) {
                    e.preventDefault()

                    $('#download').css('display', 'none')
                    $('#generate').css('display', 'none')
                    $('img').css('display', 'none')
                    $('.spinner').css('display', 'block')

                    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val()
                    var dict = {"request":"python send me the image, please. - by your friend javascript :)" }
                    var json = JSON.stringify(dict)

                     $.ajax({
                        url: '',
                        headers: {'X-CSRFToken': csrfToken},
                        dataType: 'json',
                        data: json,
                        type: 'post',
                        success: function(response) {
                            $('img').attr('src', '../../../media/images/created/' + response.response).on('load', function(){
                            $('#download').attr('href', '../../../media/images/download/' + response.response)
                            $('.spinner').css('display', 'none')
                            $('#download').css('display', 'block')
                            $('#generate').css('display', 'block')
                            $('img').css('display', 'block')
                            })
                            $('span.nav-link').text(response.credits + ' Downloads Remaining')
                            if (response.credits == '0') {
                                $('#alert').html(`<a target="_blank" href="${response.siteurl}/checkout">You have no remaining credits. You can get more here.</a>`)
                                $('#alert').css('opacity', 1)
                                $('#remaining').css('display', 'none')
                                                        }

                                                    }
                                })
                    }
            )

});

