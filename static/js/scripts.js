// *** URL For AJAX Requests
var url_full = ""
var window_width = 0
var window_height = 0

$('.owl-carousel').owlCarousel({
    loop:true,
    margin:10,
    nav:false,
    autoplay:true,
    autoplayTimeout:7000,
    autoWidth:false,
    autoplayHoverPause:true,
    navText : ['<i class="fas fa-chevron-left" aria-hidden="true"></i>','<i class="fas fa-chevron-right" aria-hidden="true"></i>'],
    responsive:{
        0:{
            items:1
        },
        1024:{
            items:2
        }
    }
});



function get_url(url_base) {
  // console.log("get_url")
  // event.preventDefault();
  url_full = url_base
  // console.log(url_full)
};

// $(window).bind('load', function() {
//   // var textareas = document.getElementsByTagName("textarea");
//   var ckeditor_textarea = document.getElementsByClassName("ckeditor");
  // console.log(textareas);
  // console.log(ckeditor_textarea);



//   $(ckeditor_textarea).each(function(index){
//       // $( this ).addClass( "ckeditor" );
//       console.log($(this).attr("id"));
//       CKEDITOR.replace( $(this).attr("id") );
//       CKEDITOR.config.toolbarGroups = [
//         { name: 'document', groups: [ 'mode', 'document', 'doctools' ] },
//         { name: 'clipboard', groups: [ 'clipboard', 'undo' ] },
//         { name: 'forms', groups: [ 'forms' ] },
//         { name: 'styles', groups: [ 'styles' ] },
//         { name: 'basicstyles', groups: [ 'basicstyles', 'cleanup' ] },
        
//         { name: 'links', groups: [ 'links' ] },
//         { name: 'paragraph', groups: [ 'list', 'indent', 'blocks', 'align', 'bidi', 'paragraph' ] },
//         { name: 'insert', groups: [ 'insert' ] },
//         { name: 'editing', groups: [ 'find', 'selection', 'spellchecker', 'editing' ] },
//         '/',
//         { name: 'colors', groups: [ 'colors' ] },
//         { name: 'tools', groups: [ 'tools' ] },
//         { name: 'others', groups: [ 'others' ] },
//         { name: 'about', groups: [ 'about' ] }
//       ];

//       CKEDITOR.config.removeButtons = 'Source,Save,Templates,Cut,Undo,Form,NewPage,ExportPdf,Preview,Print,PasteFromWord,PasteText,Paste,Copy,Redo,Checkbox,Radio,TextField,Textarea,Select,Button,ImageButton,HiddenField,Strike,Subscript,Superscript,CopyFormatting,RemoveFormat,Language,BidiRtl,BidiLtr,Anchor,Image,Flash,Table,Smiley,PageBreak,Iframe,TextColor,Maximize,About,ShowBlocks,BGColor';      
//         });  
// });


// $(window).bind('load', function() {
//   window_width = $( window ).width();
//   window_height = $( window ).height();
//   console.log("here");
// });



// $(function(){
//   window.onload = (event) => {
//     var project_slideshow = document.getElementById('project_slideshow');
//     // console.log(window_width, window_height);


//     // alert("Your screen resolution is: " + screen.width + "x" + screen.height);
//     if (project_slideshow){
//       console.log("yes right page");
//       window_width = $( window ).width();
//       window_height = $( window ).height();

//       console.log(window_width, window_height);
    

//     }

//   };
// });




// *** Editable Selects
$('#id_project_category').editableSelect();

$('#id_image_type').editableSelect();

// *** Sortable Images
window.onload = (event) => {
    var all_images = document.getElementById('all_images');

    if (all_images){
      new Sortable(all_images, {
          animation: 150,
          handle: '.icon_arrow',
          ghostClass: 'blue-background-class',
            onEnd: function (evt) {
              $.ordering(evt)
            // var itemEl = evt.item; // dragged HTMLElement
            // evt.to; // target list
            // evt.from; // previous list
            // evt.oldIndex; // element's old index within old parent
            // evt.newIndex; // element's new index within new parent
            // evt.oldDraggableIndex; // element's old index within old parent, only counting draggable elements
            // evt.newDraggableIndex; // element's new index within new parent, only counting draggable elements
            // evt.clone; // the clone element
            // evt.pullMode; // when item is in another sortable: `"clone"` if cloning, `true` if moving
          },
        });
    }
};

$.ordering = function(evt) {
    var all_images_div = document.getElementById('all_images');

    all_images_children = $(all_images_div).children();
    var images_data = [];    

    $(all_images_children).each(function(index){
        var image_info = new Object();
        var image_element = $(this)
        image_order = $( image_element ).find(".order_number");
        $(image_order).text(index);
        image_info.image_id = parseInt($(image_element).attr("value"));
        image_info.order = parseInt($( image_element ).find(".order_number").text());
        images_data.push(image_info);
    });

    images_data = JSON.stringify(images_data);

    $.ajax({
      type: 'GET',
      url: url_full,
      data: {"images_data": images_data},
      success: function (response) {
        if(response["valid"]){
          $("#section_title_header").text("All Images -- Order Adjusted");                                     
        }
      },
      error: function (response) {
          console.log(response)
      }
    }) 
  };

// *** Publish Projects, Albums, Images

$(".publish_this").click(function(e){
    e.preventDefault();

    var target_id = e.target.value;
    var check_div = $('#' + e.target.id);

    var pathname = window.location.pathname

    if (pathname.includes("projects_admin")){
      $.publish_projects_admin(target_id, check_div)}
    else if (pathname.includes("albums_admin")){
      $.publish_albums_admin(target_id, check_div)}
    else if (pathname.includes("album_images")){
      if(check_div.prop("id").includes("publish_image")){
        $.publish_images(target_id, check_div)
      }   
    }
    else{
      console.log("myadmin");
    }
  });

$.publish_myadmin_home = function(evt) {

};

$.publish_projects_admin = function(target_id, check_div) {
  var not_pub_div = $("#pending_posts");
  var pub_div = $("#published_posts");
  var no_pending = $("#none_found_pending");
  var no_published = $("#none_found_published");
  var all_parents = $( check_div ).parents();
  var area_div = all_parents[4];
  var entry_div = all_parents[3];

    $.ajax({
      type: 'GET',
      url: url_full,
      data: {"target_id": target_id},
      success: function (response) {
        if(response["valid"]){

          if (area_div.id == "published_posts"){
            not_pub_div.prepend(entry_div);
            check_div.prop("checked", false)
          } 
          else{
            pub_div.prepend(entry_div);
            check_div.prop("checked", true);
          }

          var projects_pending_posts_length = not_pub_div.children().length;
          var projects_published_post_length = pub_div.children().length;          

          if (projects_pending_posts_length > 1){
                no_pending.css("display", "none");} 
          else{no_pending.css("display", "grid");}

          if (projects_published_post_length > 1){
            no_published.css("display", "none");} 
            else{no_published.css("display", "grid");}                           
        }
      },
      error: function (response) {
          console.log(response)
      }
    }) 
};


$.publish_albums_admin = function(target_id, check_div) {
  console.log("Albums now in the actual function");
  var not_pub_div = $("#pending_albums");
  var pub_div = $("#published_albums");
  var no_pending = $("#none_found_pending");
  var no_published = $("#none_found_published");
  var all_parents = $( check_div ).parents();
  var area_div = all_parents[4];
  var entry_div = all_parents[3];

    $.ajax({
      type: 'GET',
      url: url_full,
      data: {"target_id": target_id},
      success: function (response) {
        if(response["valid"]){

          if (area_div.id == "published_albums"){
            not_pub_div.prepend(entry_div);
            check_div.prop("checked", false)} 
          else{
            pub_div.prepend(entry_div);
            check_div.prop("checked", true);
          }
          

          var albums_pending_album_length = not_pub_div.children().length;
          var albums_published_album_length = pub_div.children().length;

          if (albums_pending_album_length > 1){
                 no_pending.css("display", "none");
               } else{
                 no_pending.css("display", "grid");
               }

          if (albums_published_album_length > 1){
                 no_published.css("display", "none");
               } else{
                 no_published.css("display", "grid");
               }                                    
        }
      },
      error: function (response) {
          console.log(response)
      }
    })
};

$.publish_images = function(target_id, check_div) {
    $.ajax({
      type: 'GET',
      url: url_full,
      data: {"target_id": target_id},
      success: function (response) {
        if(response["valid"]){

          var status = response["status"];

          switch (status) { 
            case false: 
              check_div.prop("checked", false);
              break;
            case true: 
              check_div.prop("checked", true);
              break;
          }                               
        }
      },
      error: function (response) {
          console.log(response)
      }
    })
};

$(".default_radio").click(function(e){
    $('.default_radio').not(this).prop('checked', false);
    
    var target_id = e.target.value;
    var check_div = $('#' + e.target.id);
    $.default_image(target_id, check_div)
  });

$.default_image = function(target_id, check_div) {

    var all_images_div = document.getElementById('all_images');

    album_id = parseInt($(all_images_div).attr("value"));  

    all_images_children = $(all_images_div).children();
    var images_data = []; 
    images_data.push(album_id);   

    $(all_images_children).each(function(index){
        var image_info = new Object();
        var image_element = $(this)
        image_default_status = $( image_element ).find(".default_radio").prop('checked');
        
        image_info.image_id = parseInt($(image_element).attr("value"));
        image_info.default_image = image_default_status;
        if (image_info.image_id){
         images_data.push(image_info); 
        }
        
    });

    images_data = JSON.stringify(images_data);

    $.ajax({
      type: 'GET',
      url: url_full,
      data: {"images_data": images_data},
      success: function (response) {
        if(response["valid"]){
          if(response["status"] == "Success"){
            $("#section_title_header").text("All Images -- Default Image Updated");                                     
          }                              
        }
      },
      error: function (response) {
          console.log(response)
      }
    })
};


//*** Add Language AJAX
$("#add_lang_btn").click(function (e) {
  console.log("Language")
  e.preventDefault();

  var new_language = $("#id_new_language").val();

  if (new_language != ""){
    $.ajax({
      type: 'GET',
      url: url_full,
      data: {"new_language": new_language},
      success: function (response) {
          if(!response["valid"]){
              var new_language = $("#id_new_language");
              new_language.val("")
              new_language.focus()                    
          }
          else{

            id = (response['id'])
            new_lang = (response['language'])
            new_label = $("<label></label>").text(new_lang);
            new_label.addClass('label_field3');
            new_label.addClass('pb-1');

            new_check = $("<input type='checkbox' name='languages' checked></input>");

            new_check.addClass('check_form_control3');
            new_option = "option" + (response['id'])
            new_check.attr('id', new_option);
            new_check.attr('value', id);

            div_new = $("<div class = 'item vertical_grid center_h_v'></div>")
            
            div_new.append(new_label);
            div_new.append(new_check);


            $("#all_languages").prepend(div_new);
            $("#add_language").css('display', 'none');
            var new_language = $("#id_new_language");
            new_language.val("")
          }
      },
      error: function (response) {
          console.log(response)
      }
    })
  }
});

//*** Add Status AJAX
$("#add_stat_btn").click(function (e) {
  console.log("Status")
  e.preventDefault();

  var new_status = $("#id_new_status").val();

  if (new_status != ""){
    $.ajax({
      type: 'GET',
      url: url_full,
      data: {"new_status": new_status},
      success: function (response) {
          if(!response["valid"]){
              var new_status = $("#id_new_status");
              new_status.val("")
              new_status.focus()                    
          }
          else{
            console.log("ID", response['id'])
            console.log("Status", response['status'])
            id = (response['id'])
            new_stat = (response['status'])
            new_label = $("<label></label>").text(new_stat);
            new_label.addClass('label_field3');
            new_label.addClass('pb-1');

            new_check = $("<input type='checkbox' name='status' checked></input>");

            new_check.addClass('check_form_control3');
            new_option = "option" + (response['id'])
            new_check.attr('id', new_option);
            new_check.attr('value', id);

            div_new = $("<div class = 'item vertical_grid center_h_v'></div>")
            
            div_new.append(new_label);
            div_new.append(new_check);


            $("#all_status").prepend(div_new);
            $("#add_status").css('display', 'none');
            var new_status = $("#id_new_status");
            new_status.val("")
          }
      },
      error: function (response) {
          console.log(response)
      }
    })
  }
});






// $(function(){
//   $(".publish_post").click(function (e) {
//     e.preventDefault();

//     var page = ""

//     var not_pub_div = $("#pending_posts")
//     var pub_div = $("#published_posts")
//     var pending_posts_home = $("#pending_posts_home")
//     var no_pending_home_projects = $("#none_found_pending_projects")
//     var no_pending = $("#none_found_pending")
//     var no_published = $("#none_found_published")
//     var pending_project_count = $("#pending_project_count")
//     var published_project_count = $("#published_project_count")

//     var post_id = e.target.value;
//     check_div = $('#' + e.target.id);

//     var all_parents = $( check_div ).parents();
//     // console.log("2nd way all_parents", all_parents) 

//     var area_div = all_parents[4]
//     // console.log("2nd way area_div", area_div)
//     // console.log("2nd way area_div id", area_div.id) 

//     var entry_div = all_parents[3]
//     // console.log("entry_div", entry_div)  

//     if (area_div.id == "pending_posts" || area_div.id == "published_posts"){
//       page = "Projects"
//       // console.log("PROJECTS PAGE")
//     }

//     else if (area_div.id == "pending_albums" || area_div.id == "published_albums"){
//       page = "Albums"
//       // console.log("PROJECTS PAGE")
//     }

//     else if (area_div.id == "pending_posts_home" || area_div.id == "pending_albums_home"){
//       page = "MyAdmin"
//       // console.log("MY ADMIN HOME PAGE")
//     }

//     // console.log("The Page", page) 


    //   $.ajax({
    //   type: 'GET',
    //   url: url_full,
    //   data: {"post_id": post_id},
    //   success: function (response) {
    //     if(response["valid"]){

    //       if (area_div.id == "published_posts"){
    //         not_pub_div.prepend(entry_div);
    //         check_div.prop("checked", false)
    //       } 
    //       else if (area_div.id == "pending_posts"){
    //         pub_div.prepend(entry_div);
    //         check_div.prop("checked", true);
    //       }
    //       else if (area_div.id == "pending_posts_home"){
    //         entry_div.remove(entry_div);
    //       }

    //       var projects_pending_posts_length = not_pub_div.children().length;
    //       var projects_published_post_length = pub_div.children().length;
    //       var home_pending_posts_length = pending_posts_home.children().length;
    //       // console.log("projects_pending_posts_length", projects_pending_posts_length);
    //       // console.log("projects_published_post_length", projects_published_post_length);
    //       // console.log("home_pending_posts_length", home_pending_posts_length);

    //       if (page == "Projects"){
    //         // console.log("page is projects")
    //            if (projects_pending_posts_length > 1){
    //              no_pending.css("display", "none");
    //            } else{
    //              no_pending.css("display", "grid");
    //            }

    //            if (projects_published_post_length > 1){
    //              no_published.css("display", "none");
    //            } else{
    //              no_published.css("display", "grid");
    //            }
    //       }       

    //       else if (page == "MyAdmin"){
    //         // console.log("page is MyAdmin")
    //           if (home_pending_posts_length > 1){
    //                no_pending_home_projects.css("display", "none");
    //              } else{
    //                no_pending_home_projects.css("display", "grid");
    //              }

    //           count_pending = parseInt(pending_project_count.text())
    //           count_published = parseInt(published_project_count.text())

    //           new_count_pending = count_pending - 1
    //           new_count_published = count_published + 1

    //           pending_project_count.text(new_count_pending) 
    //           published_project_count.text(new_count_published)  


    //       }
                                      
    //     }
    //   },
    //   error: function (response) {
    //       console.log(response)
    //   }
    // })  
//   })
// })



// $(function(){
//   $(".publish_album").click(function (e) {
//     e.preventDefault();

//     var page = ""

//     var not_pub_div = $("#pending_albums")
//     var pub_div = $("#published_albums")
//     var pending_albums_home = $("#pending_albums_home")
//     var no_pending_home_albums = $("#none_found_pending_albums")
//     var no_pending = $("#none_found_pending")
//     var no_published = $("#none_found_published")
//     var pending_album_count = $("#pending_album_count")
//     var published_album_count = $("#published_album_count")

//     var album_id = e.target.value;
//     check_div = $('#' + e.target.id);

//     var all_parents = $( check_div ).parents();
//     console.log("all_parents", all_parents) 

//     var area_div = all_parents[4]
//     console.log("area_div", area_div)
//     // console.log("2nd way area_div id", area_div.id) 

//     var entry_div = all_parents[3]
//     console.log("entry_div", entry_div)  

//     if (area_div.id == "pending_posts" || area_div.id == "published_posts"){
//       page = "Projects"
//       console.log("PROJECTS PAGE")
//     }

//     else if (area_div.id == "pending_albums" || area_div.id == "published_albums"){
//       page = "Albums"
//       console.log("Albums PAGE")
//     }

//     else if (area_div.id == "pending_posts_home" || area_div.id == "pending_albums_home"){
//       page = "MyAdmin"
//       console.log("MY ADMIN HOME PAGE")
//     }

//     console.log("The Page", page) 


//       $.ajax({
//       type: 'GET',
//       url: url_full,
//       data: {"album_id": album_id},
//       success: function (response) {
//         if(response["valid"]){

//           if (area_div.id == "published_albums"){
//             not_pub_div.prepend(entry_div);
//             check_div.prop("checked", false)
//           } 
//           else if (area_div.id == "pending_albums"){
//             pub_div.prepend(entry_div);
//             check_div.prop("checked", true);
//           }
//           else if (area_div.id == "pending_albums_home"){
//             entry_div.remove(entry_div);
//           }

//           var albums_pending_album_length = not_pub_div.children().length;
//           var albums_published_album_length = pub_div.children().length;
//           var home_pending_albums_length = pending_albums_home.children().length;

//           if (page == "Albums"){
//             // console.log("page is Albums")
//                if (albums_pending_album_length > 1){
//                  no_pending.css("display", "none");
//                } else{
//                  no_pending.css("display", "grid");
//                }

//                if (albums_published_album_length > 1){
//                  no_published.css("display", "none");
//                } else{
//                  no_published.css("display", "grid");
//                }
//           }       

//           else if (page == "MyAdmin"){
//               if (home_pending_albums_length > 1){
//                    no_pending_home_albums.css("display", "none");
//                  } else{
//                    no_pending_home_albums.css("display", "grid");
//                  }

//               count_pending = parseInt(pending_album_count.text())
//               count_published = parseInt(published_album_count.text())

//               new_count_pending = count_pending - 1
//               new_count_published = count_published + 1

//               pending_album_count.text(new_count_pending) 
//               published_album_count.text(new_count_published)  




//           }
                                      
//         }
//       },
//       error: function (response) {
//           console.log(response)
//       }
//     })  
//   })
// })

