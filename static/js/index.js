$(document).ready(() => {
    $(".form-input").change(() => {
      calculateCost();
    });


    const getIncludes = () => {
      const values = {};
      $(".includes").each((index, element) => {
        values[$(element).attr("name")] = $(element).val();
      });
      return values;
    };

    const includes = getIncludes()
    

    $("#moodboard").on('change', () => {
      if ($("#moodboard").is(':checked')) {
        $("#moodboard").attr('value', 'true');
        $("#moodboard").attr('value', 'true');
        $("#moodboard_days").prop('disabled', false);
        $("#moodboard_days").removeClass('border-gray-200 text-red-200 placeholder-red-200');
        $("#moodboard_artists").removeClass('border-gray-200 text-red-200 placeholder-red-200');
        $("#moodboard_days").addClass('shadow');
        $("#moodboard_artists").addClass('shadow');
        $("#moodboard_artists").prop('disabled', false);
        $(".moodboard_section").removeClass('hidden')
        $(".moodboard_text").text('Enable')
      } else {
        $("#moodboard").attr('value', 'false');
        $(".moodboard_text").text('Disable')
        $("#moodboard_days").prop('disabled', true);
        $("#moodboard_artists").prop('disabled', true);
        $("#moodboard_days").addClass('border-gray-200 text-red-200 placeholder-red-200');
        $("#moodboard_artists").addClass('border-gray-200 text-red-200 placeholder-red-200');
        $("#moodboard_days").removeClass('shadow');
        $("#moodboard_artists").removeClass('shadow');
        $(".moodboard_section").addClass('hidden')
        $("input[name='moodboard_days']").val('0')
        $("input[name='moodboard_artists']").val('0')
        
      }
      includes["moodboard"] = ($("#moodboard").val())
    });


    $("#illustration").on('change', () => {
      if ($("#illustration").is(':checked')) {
        $("#illustration").attr('value', 'true');
        $("#illustration_days").prop('disabled', false);
        $("#illustration_days").removeClass('border-gray-200 text-red-200 placeholder-red-200');
        $("#illustration_artists").removeClass('border-gray-200 text-red-200 placeholder-red-200');
        $("#illustration_days").addClass('shadow');
        $("#illustration_artists").addClass('shadow');
        $("#illustration_artists").prop('disabled', false);
        $(".illustration_section").removeClass('hidden')
        $(".illustration_text").text('Enable')
      } else {
        $("#illustration").attr('value', 'false');
        $(".illustration_text").text('Disable')
        $("#illustration_days").prop('disabled', true);
        $("#illustration_artists").prop('disabled', true);
        $("#illustration_days").addClass('border-gray-200 text-red-200 placeholder-red-200');
        $("#illustration_artists").addClass('border-gray-200 text-red-200 placeholder-red-200');
        $("#illustration_days").removeClass('shadow');
        $("#illustration_artists").removeClass('shadow');
        $(".illustration_section").addClass('hidden')
        $("input[name='illustration_days']").val('0')
        $("input[name='illustration_artists']").val('0')
      }

      includes["moodboard"] = ($("#moodboard").val())


    });

    $("#modelling").on('change', () => {
      if ($("#modelling").is(':checked')) {
        $("#modelling").attr('value', 'true');
        $("#modelling_days").prop('disabled', false);
        $("#modelling_days").removeClass('border-gray-200 text-red-200 placeholder-red-200');
        $("#modelling_artists").removeClass('border-gray-200 text-red-200 placeholder-red-200');
        $("#modelling_days").addClass('shadow');
        $("#modelling_artists").addClass('shadow');
        $("#modelling_artists").prop('disabled', false);
        $(".modelling_section").removeClass('hidden');
        $(".modelling_text").text('Enable');
      } else {
        $("#modelling").attr('value', 'false');
        $(".modelling_text").text('Disable');
        $("#modelling_days").prop('disabled', true);
        $("#modelling_artists").prop('disabled', true);
        $("#modelling_days").addClass('border-gray-200 text-red-200 placeholder-red-200');
        $("#modelling_artists").addClass('border-gray-200 text-red-200 placeholder-red-200');
        $("#modelling_days").removeClass('shadow');
        $("#modelling_artists").removeClass('shadow');
        $(".modelling_section").addClass('hidden');
        $("input[name='modelling_days']").val('0')
        $("input[name='modelling_artists']").val('0')
      }
      includes["modelling"] = ($("#modelling").val());
      
    });

    $("#rigging").on('change', () => {
      if ($("#rigging").is(':checked')) {
        $("#rigging").attr('value', 'true');
        $("#rigging_days").prop('disabled', false);
        $("#rigging_days").removeClass('border-gray-200 text-red-200 placeholder-red-200');
        $("#rigging_artists").removeClass('border-gray-200 text-red-200 placeholder-red-200');
        $("#rigging_days").addClass('shadow');
        $("#rigging_artists").addClass('shadow');
        $("#rigging_artists").prop('disabled', false);
        $(".rigging_section").removeClass('hidden');
        $(".rigging_text").text('Enable');
      } else {
        $("#rigging").attr('value', 'false');
        $(".rigging_text").text('Disable');
        $("#rigging_days").prop('disabled', true);
        $("#rigging_artists").prop('disabled', true);
        $("#rigging_days").addClass('border-gray-200 text-red-200 placeholder-red-200');
        $("#rigging_artists").addClass('border-gray-200 text-red-200 placeholder-red-200');
        $("#rigging_days").removeClass('shadow');
        $("#rigging_artists").removeClass('shadow');
        $(".rigging_section").addClass('hidden');
        $("input[name='rigging_days']").val('0')
        $("input[name='rigging_artists']").val('0')
      }
      includes["rigging"] = ($("#rigging").val());
    });

    $("#storyboard").on('change', () => {
      if ($("#storyboard").is(':checked')) {
        $("#storyboard").attr('value', 'true');
        $("#storyboard_days").prop('disabled', false);
        $("#storyboard_days").removeClass('border-gray-200 text-red-200 placeholder-red-200');
        $("#storyboard_artists").removeClass('border-gray-200 text-red-200 placeholder-red-200');
        $("#storyboard_days").addClass('shadow');
        $("#storyboard_artists").addClass('shadow');
        $("#storyboard_artists").prop('disabled', false);
        $(".storyboard_section").removeClass('hidden');
        $(".storyboard_text").text('Enable');
      } else {
        $("#storyboard").attr('value', 'false');
        $(".storyboard_text").text('Disable');
        $("#storyboard_days").prop('disabled', true);
        $("#storyboard_artists").prop('disabled', true);
        $("#storyboard_days").addClass('border-gray-200 text-red-200 placeholder-red-200');
        $("#storyboard_artists").addClass('border-gray-200 text-red-200 placeholder-red-200');
        $("#storyboard_days").removeClass('shadow');
        $("#storyboard_artists").removeClass('shadow');
        $(".storyboard_section").addClass('hidden');
        $("input[name='storyboard_days']").val('0')
        $("input[name='storyboard_artists']").val('0')
      }
      includes["storyboard"] = ($("#storyboard").val());

    });


    $("#texturing").on('change', () => {
      if ($("#texturing").is(':checked')) {
        $("#texturing").attr('value', 'true');
        $("#texturing_days").prop('disabled', false);
        $("#texturing_days").removeClass('border-gray-200 text-red-200 placeholder-red-200');
        $("#texturing_artists").removeClass('border-gray-200 text-red-200 placeholder-red-200');
        $("#texturing_days").addClass('shadow');
        $("#texturing_artists").addClass('shadow');
        $("#texturing_artists").prop('disabled', false);
        $(".texturing_section").removeClass('hidden');
        $(".texturing_text").text('Enable');
      } else {
        $("#texturing").attr('value', 'false');
        $(".texturing_text").text('Disable');
        $("#texturing_days").prop('disabled', true);
        $("#texturing_artists").prop('disabled', true);
        $("#texturing_days").addClass('border-gray-200 text-red-200 placeholder-red-200');
        $("#texturing_artists").addClass('border-gray-200 text-red-200 placeholder-red-200');
        $("#texturing_days").removeClass('shadow');
        $("#texturing_artists").removeClass('shadow');
        $(".texturing_section").addClass('hidden');
        $("input[name='texturing_days']").val('0')
        $("input[name='texturing_artists']").val('0')
        
      }
      includes["texturing"] = ($("#texturing").val());
    });

    $("#lookdev").on('change', () => {
      if ($("#lookdev").is(':checked')) {
        $("#lookdev").attr('value', 'true');
        $("#lookdev_days").prop('disabled', false);
        $("#lookdev_days").removeClass('border-gray-200 text-red-200 placeholder-red-200');
        $("#lookdev_artists").removeClass('border-gray-200 text-red-200 placeholder-red-200');
        $("#lookdev_days").addClass('shadow');
        $("#lookdev_artists").addClass('shadow');
        $("#lookdev_artists").prop('disabled', false);
        $(".lookdev_section").removeClass('hidden');
        $(".lookdev_text").text('Enable');
      } else {
        $("#lookdev").attr('value', 'false');
        $(".lookdev_text").text('Disable');
        $("#lookdev_days").prop('disabled', true);
        $("#lookdev_artists").prop('disabled', true);
        $("#lookdev_days").addClass('border-gray-200 text-red-200 placeholder-red-200');
        $("#lookdev_artists").addClass('border-gray-200 text-red-200 placeholder-red-200');
        $("#lookdev_days").removeClass('shadow');
        $("#lookdev_artists").removeClass('shadow');
        $(".lookdev_section").addClass('hidden');
        $("input[name='lookdev_days']").val('0')
        $("input[name='lookdev_artists']").val('0')
      }
      includes["lookdev"] = ($("#lookdev").val());
    });


    $("#layout").on('change', () => {
      if ($("#layout").is(':checked')) {
        $("#layout").attr('value', 'true');
        $("#layout_days").prop('disabled', false);
        $("#layout_days").removeClass('border-gray-200 text-red-200 placeholder-red-200');
        $("#layout_artists").removeClass('border-gray-200 text-red-200 placeholder-red-200');
        $("#layout_days").addClass('shadow');
        $("#layout_artists").addClass('shadow');
        $("#layout_artists").prop('disabled', false);
        $(".layout_section").removeClass('hidden');
        $(".layout_text").text('Enable');
      } else {
        $("#layout").attr('value', 'false');
        $(".layout_text").text('Disable');
        $("#layout_days").prop('disabled', true);
        $("#layout_artists").prop('disabled', true);
        $("#layout_days").addClass('border-gray-200 text-red-200 placeholder-red-200');
        $("#layout_artists").addClass('border-gray-200 text-red-200 placeholder-red-200');
        $("#layout_days").removeClass('shadow');
        $("#layout_artists").removeClass('shadow');
        $(".layout_section").addClass('hidden');
        $("input[name='layout_days']").val('0')
        $("input[name='layout_artists']").val('0')
      }
      includes["layout"] = ($("#layout").val());
    });

    $("#animation").on('change', () => {
      if ($("#animation").is(':checked')) {
        $("#animation").attr('value', 'true');
        $("#animation_days").prop('disabled', false);
        $("#animation_days").removeClass('border-gray-200 text-red-200 placeholder-red-200');
        $("#animation_artists").removeClass('border-gray-200 text-red-200 placeholder-red-200');
        $("#animation_days").addClass('shadow');
        $("#animation_artists").addClass('shadow');
        $("#animation_artists").prop('disabled', false);
        $(".animation_section").removeClass('hidden');
        $(".animation_text").text('Enable');
      } else {
        $("#animation").attr('value', 'false');
        $(".animation_text").text('Disable');
        $("#animation_days").prop('disabled', true);
        $("#animation_artists").prop('disabled', true);
        $("#animation_days").addClass('border-gray-200 text-red-200 placeholder-red-200');
        $("#animation_artists").addClass('border-gray-200 text-red-200 placeholder-red-200');
        $("#animation_days").removeClass('shadow');
        $("#animation_artists").removeClass('shadow');
        $(".animation_section").addClass('hidden');
        $("input[name='animation_days']").val('0')
        $("input[name='animation_artists']").val('0')
      }
      includes["animation"] = ($("#animation").val());
    });

    $("#lighting").on('change', () => {
      if ($("#lighting").is(':checked')) {
        $("#lighting").attr('value', 'true');
        $("#lighting_days").prop('disabled', false);
        $("#lighting_days").removeClass('border-gray-200 text-red-200 placeholder-red-200');
        $("#lighting_artists").removeClass('border-gray-200 text-red-200 placeholder-red-200');
        $("#lighting_days").addClass('shadow');
        $("#lighting_artists").addClass('shadow');
        $("#lighting_artists").prop('disabled', false);
        $(".lighting_section").removeClass('hidden');
        $(".lighting_text").text('Enable');
      } else {
        $("#lighting").attr('value', 'false');
        $(".lighting_text").text('Disable');
        $("#lighting_days").prop('disabled', true);
        $("#lighting_artists").prop('disabled', true);
        $("#lighting_days").addClass('border-gray-200 text-red-200 placeholder-red-200');
        $("#lighting_artists").addClass('border-gray-200 text-red-200 placeholder-red-200');
        $("#lighting_days").removeClass('shadow');
        $("#lighting_artists").removeClass('shadow');
        $(".lighting_section").addClass('hidden');
        $("input[name='lighting_days']").val('0')
        $("input[name='lighting_artists']").val('0')
      }
      includes["lighting"] = ($("#lighting").val());
    });

    $("#rendering").on('change', () => {
      if ($("#rendering").is(':checked')) {
        $("#rendering").attr('value', 'true');
        $("#rendering_days").prop('disabled', false);
        $("#rendering_days").removeClass('border-gray-200 text-red-200 placeholder-red-200');
        $("#rendering_artists").removeClass('border-gray-200 text-red-200 placeholder-red-200');
        $("#rendering_days").addClass('shadow');
        $("#rendering_artists").addClass('shadow');
        $("#rendering_artists").prop('disabled', false);
        $(".rendering_section").removeClass('hidden');
        $(".rendering_text").text('Enable');
      } else {
        $("#rendering").attr('value', 'false');
        $(".rendering_text").text('Disable');
        $("#rendering_days").prop('disabled', true);
        $("#rendering_artists").prop('disabled', true);
        $("#rendering_days").addClass('border-gray-200 text-red-200 placeholder-red-200');
        $("#rendering_artists").addClass('border-gray-200 text-red-200 placeholder-red-200');
        $("#rendering_days").removeClass('shadow');
        $("#rendering_artists").removeClass('shadow');
        $(".rendering_section").addClass('hidden');
        $("input[name='rendering_days']").val('0')
        $("input[name='rendering_artists']").val('0')
      }
      includes["rendering"] = ($("#rendering").val());
    });


    $("#fx").on('change', () => {
      if ($("#fx").is(':checked')) {
        $("#fx").attr('value', 'true');
        $("#fx_days").prop('disabled', false);
        $("#fx_days").removeClass('border-gray-200 text-red-200 placeholder-red-200');
        $("#fx_artists").removeClass('border-gray-200 text-red-200 placeholder-red-200');
        $("#fx_days").addClass('shadow');
        $("#fx_artists").addClass('shadow');
        $("#fx_artists").prop('disabled', false);
        $(".fx_section").removeClass('hidden');
        $(".fx_text").text('Enable');
      } else {
        $("#fx").attr('value', 'false');
        $(".fx_text").text('Disable');
        $("#fx_days").prop('disabled', true);
        $("#fx_artists").prop('disabled', true);
        $("#fx_days").addClass('border-gray-200 text-red-200 placeholder-red-200');
        $("#fx_artists").addClass('border-gray-200 text-red-200 placeholder-red-200');
        $("#fx_days").removeClass('shadow');
        $("#fx_artists").removeClass('shadow');
        $(".fx_section").addClass('hidden');
        $("input[name='fx_days']").val('0')
        $("input[name='fx_artists']").val('0')
      }
      includes["fx"] = ($("#fx").val());
    });

    $("#compositing").on('change', () => {
      if ($("#compositing").is(':checked')) {
        $("#compositing").attr('value', 'true');
        $("#compositing_days").prop('disabled', false);
        $("#compositing_days").removeClass('border-gray-200 text-red-200 placeholder-red-200');
        $("#compositing_artists").removeClass('border-gray-200 text-red-200 placeholder-red-200');
        $("#compositing_days").addClass('shadow');
        $("#compositing_artists").addClass('shadow');
        $("#compositing_artists").prop('disabled', false);
        $(".compositing_section").removeClass('hidden');
        $(".compositing_text").text('Enable');
      } else {
        $("#compositing").attr('value', 'false');
        $(".compositing_text").text('Disable');
        $("#compositing_days").prop('disabled', true);
        $("#compositing_artists").prop('disabled', true);
        $("#compositing_days").addClass('border-gray-200 text-red-200 placeholder-red-200');
        $("#compositing_artists").addClass('border-gray-200 text-red-200 placeholder-red-200');
        $("#compositing_days").removeClass('shadow');
        $("#compositing_artists").removeClass('shadow');
        $(".compositing_section").addClass('hidden');
        $("input[name='compositing_days']").val('0')
        $("input[name='compositing_artists']").val('0')
      }
      includes["compositing"] = ($("#compositing").val());
    });

    $("#audio_studio").on('change', () => {
      if ($("#audio_studio").is(':checked')) {
        $("#audio_studio").attr('value', 'true');
        $("#audio_studio_days").prop('disabled', false);
        $("#audio_studio_days").removeClass('border-gray-200 text-red-200 placeholder-red-200');
        $("#audio_studio_artists").removeClass('border-gray-200 text-red-200 placeholder-red-200');
        $("#audio_studio_days").addClass('shadow');
        $("#audio_studio_artists").addClass('shadow');
        $("#audio_studio_artists").prop('disabled', false);
        $(".audio_studio_section").removeClass('hidden');
        $(".audio_studio_text").text('Enable');
      } else {
        $("#audio_studio").attr('value', 'false');
        $(".audio_studio_text").text('Disable');
        $("#audio_studio_days").prop('disabled', true);
        $("#audio_studio_artists").prop('disabled', true);
        $("#audio_studio_days").addClass('border-gray-200 text-red-200 placeholder-red-200');
        $("#audio_studio_artists").addClass('border-gray-200 text-red-200 placeholder-red-200');
        $("#audio_studio_days").removeClass('shadow');
        $("#audio_studio_artists").removeClass('shadow');
        $(".audio_studio_section").addClass('hidden');
        $("input[name='audio_studio_days']").val('0')
        $("input[name='audio_studio_artists']").val('0')
      }
      includes["audio_studio"] = ($("#audio_studio").val());
    });

    $("#music_sync").on('change', () => {
      if ($("#music_sync").is(':checked')) {
        $("#music_sync").attr('value', 'true');
        $("#music_sync_days").prop('disabled', false);
        $("#music_sync_days").removeClass('border-gray-200 text-red-200 placeholder-red-200');
        $("#music_sync_artists").removeClass('border-gray-200 text-red-200 placeholder-red-200');
        $("#music_sync_days").addClass('shadow');
        $("#music_sync_artists").addClass('shadow');
        $("#music_sync_artists").prop('disabled', false);
        $(".music_sync_section").removeClass('hidden');
        $(".music_sync_text").text('Enable');
      } else {
        $("#music_sync").attr('value', 'false');
        $(".music_sync_text").text('Disable');
        $("#music_sync_days").prop('disabled', true);
        $("#music_sync_artists").prop('disabled', true);
        $("#music_sync_days").addClass('border-gray-200 text-red-200 placeholder-red-200');
        $("#music_sync_artists").addClass('border-gray-200 text-red-200 placeholder-red-200');
        $("#music_sync_days").removeClass('shadow');
        $("#music_sync_artists").removeClass('shadow');
        $(".music_sync_section").addClass('hidden');
        $("input[name='music_sync_days']").val('0')
        $("input[name='music_sync_artists']").val('0')
      }
      includes["music_sync"] = ($("#music_sync").val());
    });


    $("#editing").on('change', () => {
      if ($("#editing").is(':checked')) {
        $("#editing").attr('value', 'true');
        $("#editing_days").prop('disabled', false);
        $("#editing_days").removeClass('border-gray-200 text-red-200 placeholder-red-200');
        $("#editing_artists").removeClass('border-gray-200 text-red-200 placeholder-red-200');
        $("#editing_days").addClass('shadow');
        $("#editing_artists").addClass('shadow');
        $("#editing_artists").prop('disabled', false);
        $(".editing_section").removeClass('hidden');
        $(".editing_text").text('Enable');
      } else {
        $("#editing").attr('value', 'false');
        $(".editing_text").text('Disable');
        $("#editing_days").prop('disabled', true);
        $("#editing_artists").prop('disabled', true);
        $("#editing_days").addClass('border-gray-200 text-red-200 placeholder-red-200');
        $("#editing_artists").addClass('border-gray-200 text-red-200 placeholder-red-200');
        $("#editing_days").removeClass('shadow');
        $("#editing_artists").removeClass('shadow');
        $(".editing_section").addClass('hidden');
        $("input[name='editing_days']").val('0')
        $("input[name='editing_artists']").val('0')
      }
      includes["editing"] = ($("#editing").val());
    });

    $("#motion").on('change', () => {
      if ($("#motion").is(':checked')) {
        $("#motion").attr('value', 'true');
        $("#motion_days").prop('disabled', false);
        $("#motion_days").removeClass('border-gray-200 text-red-200 placeholder-red-200');
        $("#motion_artists").removeClass('border-gray-200 text-red-200 placeholder-red-200');
        $("#motion_days").addClass('shadow');
        $("#motion_artists").addClass('shadow');
        $("#motion_artists").prop('disabled', false);
        $(".motion_section").removeClass('hidden');
        $(".motion_text").text('Enable');
      } else {
        $("#motion").attr('value', 'false');
        $(".motion_text").text('Disable');
        $("#motion_days").prop('disabled', true);
        $("#motion_artists").prop('disabled', true);
        $("#motion_days").addClass('border-gray-200 text-red-200 placeholder-red-200');
        $("#motion_artists").addClass('border-gray-200 text-red-200 placeholder-red-200');
        $("#motion_days").removeClass('shadow');
        $("#motion_artists").removeClass('shadow');
        $(".motion_section").addClass('hidden');
        $("input[name='motion_days']").val('0')
        $("input[name='motion_artists']").val('0')
      }
      includes["motion"] = ($("#motion").val());
    });

    $("#voiceover").on('change', () => {
      if ($("#voiceover").is(':checked')) {
        $("#voiceover").attr('value', 'true');
        $("#voiceover_salary").prop('disabled', false);
        $("#voiceover_salary").removeClass('border-gray-200 text-red-200 placeholder-red-200');
        $("#voiceover_salary").addClass('shadow');
        $(".voiceover_section").removeClass('hidden');
        $(".voiceover_text").text('Enable');
      } else {
        $("#voiceover").attr('value', 'false');
        $(".voiceover_text").text('Disable');
        $("#voiceover_salary").prop('disabled', true);
        $("#voiceover_salary").addClass('border-gray-200 text-red-200 placeholder-red-200');
        $("#voiceover_salary").removeClass('shadow');
        $(".voiceover_section").addClass('hidden');
        $("input[name='voiceover_days']").val('0')
        $("input[name='voiceover_artists']").val('0')
      }
      includes["voiceover"] = ($("#voiceover").val());
    });




    $(".submit-form").click(() => {
      getForm();
    });

    $(".preproduction_btn_next").click(() => {
      $(".preproduction").addClass("hidden");
        $(".production").removeClass("hidden");
  
    });

    $(".preproduction_btn_prev").click(() => {
      $(".preproduction").addClass("hidden");
      $(".initialize").removeClass("hidden");
    });

    $(".init_next").click(() => {
      $(".preproduction").removeClass("hidden");
      $(".initialize").addClass("hidden");
    });

  
    $(".prod_btn_prev").click(() => {
      $(".production").addClass("hidden");
      $(".preproduction").removeClass("hidden");  
    });

    $(".prod_btn_next").click(() => {
      $(".production").addClass("hidden");
      $(".postproduction").removeClass("hidden");
    });

    $(".sum_btn_prev").click(() => {
      $(".voice").removeClass("hidden");
      $(".get_price").addClass("hidden");
    });


    $(".post_prod_btn_prev").click(() => {
      $(".production").removeClass("hidden");
      $(".postproduction").addClass("hidden");
    });

    $(".post_prod_btn_next").click(() => {
      $(".postproduction").addClass("hidden");
      $(".voice").removeClass("hidden");
    });

    $(".summary_prev_button").click(() => {
      $(".voice").removeClass("hidden");
      $(".get_price").addClass("hidden");
    });

    $(".voice_button_next").click(() => {
      $(".voice").addClass("hidden");
      $(".sub_summary").addClass("hidden");
      $(".invoice_detail").removeClass("hidden");
    });

    $(".voice_button_prev").click(() => {
      $(".voice").addClass("hidden");
      $(".postproduction").removeClass("hidden");
    });



    const calculateCost = () => {
      const variables = getFormValues()
      variables['value_added_tax'] = $("input[name='value_added_tax']:checked").val()
      for (const [key, value] of Object.entries(includes)) {
        variables[key] = value
      }
      console.log(variables)
      $.ajax({
        url: '{% url "accounts:summary" %}',
        method: "GET",
        data: variables,
        traditional: true,
        success: (data) => {
          $(".summary").html(data);
        },
        error: (error) => {
          console.log("There is an error with your JS code");
        },
      });
    };


    const getFormValues = () => {
      const values = {};
      $(".form-input").each((index, element) => {
        values[$(element).attr("name")] = $(element).val();
      });
      return values;
    };

    const getForm = () => {
      const prices = getPrices();

      $.ajax({
        url: '{% url "accounts:invoice" %}',
        method: "POST",
        data: prices,
        traditional: true,
        success: (data) => {
          /**window.location.href = '{% url "accounts:success" %}'**/
          console.log(data);
        },
        error: (error) => {
          console.log("There is an error with your JS code");
        },
      });
    };


    const getPrices = () => {
      const values = {};
      $(".price").each((index, element) => {
        values[$(element).attr("id")] = $(element).val();
      });
      return values;
      console.log(values);
    };

    calculateCost();
  });