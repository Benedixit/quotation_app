from django.shortcuts import render, redirect
from .models import Salaries, PriceDetail, PriceInclude
from num2words import num2words


# Create your views here.
def home(request):
    return render(request, 'index.html')

def summary(request):

    
        
    if request.method == 'GET' and request.headers.get('X_REQUESTED_WITH') == 'XMLHttpRequest':

        if not Salaries.objects.filter(task="Moodboard").exists():
            Salaries.objects.create(task="Moodboard", salary=400000.00)
        if not Salaries.objects.filter(task="Storyboard").exists():
            Salaries.objects.create(task="Storyboard", salary=500000.00)
        if not Salaries.objects.filter(task="Illustration").exists():
            Salaries.objects.create(task="Illustration", salary=500000.00)
        if not Salaries.objects.filter(task="Compositing").exists():
            Salaries.objects.create(task="Compositing", salary=500000.00)
        if not Salaries.objects.filter(task="Editing").exists():
            Salaries.objects.create(task="Editing", salary=500000.00)
        if not Salaries.objects.filter(task="Motion Graphics").exists():
            Salaries.objects.create(task="Motion Graphics", salary=500000.00)
        if not Salaries.objects.filter(task="Texturing").exists():
            Salaries.objects.create(task="Texturing", salary=500000.00)
        if not Salaries.objects.filter(task="Animation").exists():
            Salaries.objects.create(task="Animation", salary=600000.00)
        if not Salaries.objects.filter(task="Rigging").exists():
            Salaries.objects.create(task="Rigging", salary=400000.00)
        if not Salaries.objects.filter(task="Lookdev").exists():
            Salaries.objects.create(task="Lookdev", salary=500000.00)
        if not Salaries.objects.filter(task="FX").exists():
            Salaries.objects.create(task="FX", salary=500000.00)
        if not Salaries.objects.filter(task="Layout").exists():
            Salaries.objects.create(task="Layout", salary=500000.00)
        if not Salaries.objects.filter(task="Lighting").exists():
            Salaries.objects.create(task="Lighting", salary=500000.00)
        if not Salaries.objects.filter(task="Rendering").exists():
            Salaries.objects.create(task="Rendering", salary=500000.00)
        if not Salaries.objects.filter(task="Audio_studio").exists():
            Salaries.objects.create(task="Audio_studio", salary=500000.00)
        if not Salaries.objects.filter(task="Music_sync").exists():
            Salaries.objects.create(task="Music_sync", salary=500000.00)
        if not Salaries.objects.filter(task="Modelling").exists():
            Salaries.objects.create(task="Modelling", salary=500000.00)

        # Gets number of artists and days in the Preproduction code
        moodboard_days = request.GET.get('moodboard_days')
        moodboard_artists = request.GET.get('moodboard_artists')
        illustration_days = request.GET.get('illustration_days')
        illustration_artists = request.GET.get('illustration_artists')
        storyboard_days = request.GET.get('storyboard_days')
        storyboard_artists = request.GET.get('storyboard_artists')


        # Gets number of artists and days in the Postproduction code
        compositing_days = request.GET.get('compositing_days')
        compositing_artists = request.GET.get('compositing_artists')
        editing_days = request.GET.get('editing_days')
        editing_artists = request.GET.get('editing_artists')
        motion_days = request.GET.get('motion_days')
        motion_artists = request.GET.get('motion_artists')

        # Gets number of artists and days in the Production code
        texturing_days = request.GET.get('texturing_days')
        animation_days = request.GET.get('animation_days')
        rigging_days = request.GET.get('rigging_days')
        lookdev_days = request.GET.get('lookdev_days')
        fx_days = request.GET.get('fx_days')
        texturing_artists = request.GET.get('texturing_artists')
        animation_artists = request.GET.get('animation_artists')
        rigging_artists = request.GET.get('rigging_artists')
        lookdev_artists = request.GET.get('lookdev_artists')
        fx_artists = request.GET.get('fx_artists')
        modelling_days = request.GET.get('modelling_days')
        modelling_artists = request.GET.get('modelling_artists')
        lighting_days = request.GET.get('lighting_days')
        lighting_artists = request.GET.get('lighting_artists')
        rendering_days = request.GET.get('rendering_days')
        rendering_artists = request.GET.get('rendering_artists')
        layout_days = request.GET.get('layout_days')
        layout_artists = request.GET.get('layout_artists')

        # Gets number of artists and days in the Voice code
        audio_studio_days = request.GET.get('audio_studio_days')
        audio_studio_artists = request.GET.get('audio_studio_artists')
        music_sync_days = request.GET.get('music_sync_days')
        music_sync_artists = request.GET.get('music_sync_artists')



        company_name = request.GET.get('company_name')
        invoice_id = request.GET.get('invoice_id')
        invoice_title = request.GET.get('invoice_title')
        company_location = request.GET.get('company_location')



        moodboard = request.GET.get('moodboard')
        illustration = request.GET.get('illustration')
        storyboard = request.GET.get('storyboard')
        compositing = request.GET.get('compositing')
        motion = request.GET.get('motion')
        modelling = request.GET.get('modelling')
        texturing = request.GET.get('texturing')
        rigging = request.GET.get('rigging')
        animation = request.GET.get('animation')
        fx = request.GET.get('fx')
        lighting = request.GET.get('lighting')
        voiceover = request.GET.get('voiceover')
        music_sync = request.GET.get('music_sync')
        audio_studio = request.GET.get('audio_studio')
        layout = request.GET.get('layout')
        lookdev = request.GET.get('lookdev')


        # Get salaries for the Preproduction tasks
        moodboard_salary = (Salaries.objects.get(task="Moodboard").salary)/19
        illustration_salary = (Salaries.objects.get(task="Illustration").salary)/19
        storyboard_salary = (Salaries.objects.get(task="Storyboard").salary)/19

        # Get salaries for the Postproduction tasks
        compositing_salary = (Salaries.objects.get(task="Compositing").salary)/19
        editing_salary = (Salaries.objects.get(task="Editing").salary)/19
        motion_salary = (Salaries.objects.get(task="Motion Graphics").salary)/19

         # Get salaries for the Production tasks
        texturing_salary = (Salaries.objects.get(task="Texturing").salary) / 19
        animation_salary = (Salaries.objects.get(task="Animation").salary) / 19
        rigging_salary = (Salaries.objects.get(task="Rigging").salary) / 19
        lookdev_salary = (Salaries.objects.get(task="Lookdev").salary) / 19
        fx_salary = (Salaries.objects.get(task="FX").salary) / 19
        modelling_salary = (Salaries.objects.get(task="Modelling").salary) / 19
        layout_salary = (Salaries.objects.get(task="Layout").salary) / 19
        lighting_salary = (Salaries.objects.get(task="Lighting").salary) / 19
        rendering_salary = (Salaries.objects.get(task="Rendering").salary) / 19

        #Get Salaries for voice tasks
        audio_studio_salary = (Salaries.objects.get(task="Audio_studio").salary)/19
        music_sync_salary = (Salaries.objects.get(task="Music_sync").salary)/19
        voiceover_salary = request.GET.get("voiceover_salary")

        



        vat = request.GET.get('value_added_tax')

        labor_cost = {
            'moodboard': float(moodboard_salary) * float(moodboard_days) * float(moodboard_artists),
            'storyboard': float(storyboard_salary) * float(storyboard_days) * float(storyboard_artists),
            'illustration': float(illustration_salary) * float(illustration_days) * float(illustration_artists),
            'texturing': float(texturing_salary) * float(texturing_days) * float(texturing_artists),
            'modelling': float(modelling_salary) * float(modelling_days) * float(modelling_artists),
            'rigging': float(rigging_salary) * float(rigging_days) * float(rigging_artists),
            'lookdev': float(lookdev_salary) * float(lookdev_days) * float(lookdev_artists),
            'layout': float(layout_salary) * float(layout_days) * float(layout_artists),
            'animation': float(animation_salary) * float(animation_days) * float(animation_artists),
            'fx': float(fx_salary) * float(fx_days) * float(fx_artists),
            'lighting': float(lighting_salary) * float(lighting_days) * float(lighting_artists),
            'rendering': float(rendering_salary) * float(rendering_days) * float(rendering_artists),
            'compositing': float(compositing_salary) * float(compositing_days) * float(compositing_artists),
            'editing': float(editing_salary) * float(editing_days) * float(editing_artists),
            'motion': float(motion_salary) * float(motion_days) * float(motion_artists),
            'audio_studio': float(audio_studio_salary) * float(audio_studio_days) * float(audio_studio_artists),
            'music_sync': float(music_sync_salary) * float(music_sync_days) * float(music_sync_artists),
            'voiceover': float(voiceover_salary)

        }


        total_salary = sum(labor_cost.values())
        total_days = request.GET.get('production_days')
        
        if total_days != 0:
            overhead = 153796.77 * float(total_days)
        else:
            overhead = 0.00
        
        profit_margin = 20

        #Preproduction stage
        if int(moodboard_artists) != 0 and int(moodboard_days) != 0:
            moodboard_price = ((int(moodboard_days)*int(moodboard_artists)*float(moodboard_salary)) \
                            + ((float(moodboard_salary)/total_salary)*overhead))*((100+profit_margin)/100)
        else:
            moodboard_price = 0.00

        if int(illustration_artists) != 0 and int(illustration_days) != 0:
            illustration_price = ((int(illustration_days)*int(illustration_artists)*float(illustration_salary)) \
                           + ((float(illustration_salary)/total_salary)*overhead))*((100+profit_margin)/100)
        else:
            illustration_price = 0.00

        if int(storyboard_artists) != 0 and int(storyboard_days) != 0:
            storyboard_price = ((int(storyboard_days)*int(storyboard_artists)*float(storyboard_salary)) \
                           + ((float(storyboard_salary)/total_salary)*overhead))*((100+profit_margin)/100)
        else:
            storyboard_price = 0.00



        #Post-production stage
        if int(compositing_artists) != 0 and int(compositing_days) != 0:
            compositing_price = ((int(compositing_days)*int(compositing_artists)*float(compositing_salary)) \
                           + ((float(compositing_salary)/total_salary)*overhead))*((100+profit_margin)/100)
        else:
            compositing_price = 0.00

        if int(editing_artists) != 0 and int(editing_days) != 0:
            editing_price = ((int(editing_days)*int(editing_artists)*float(editing_salary)) \
                           + ((float(editing_salary)/total_salary)*overhead))*((100+profit_margin)/100)
        else:
            editing_price = 0.00

        if int(motion_artists) != 0 and int(motion_days) != 0:
            motion_price = ((int(motion_days)*int(motion_artists)*float(motion_salary)) \
                           + ((float(motion_salary)/total_salary)*overhead))*((100+profit_margin)/100)
        else:
            motion_price = 0.00
        

        #Production stage
        if int(texturing_artists) != 0 and int(texturing_days) != 0:
            texturing_price = ((int(texturing_days) * int(texturing_artists) * float(texturing_salary)) +
                        ((float(texturing_salary) / total_salary) * overhead)) * ((100+profit_margin)/100)
        else:
            texturing_price = 0.00

        if int(animation_artists) != 0 and int(animation_days) != 0:
            animation_price = ((int(animation_days) * int(animation_artists) * float(animation_salary)) +
                        ((float(animation_salary) / total_salary) * overhead)) * ((100+profit_margin)/100)
        else:
            animation_price = 0.00

        if int(rigging_artists) != 0 and int(rigging_days) != 0:
            rigging_price = ((int(rigging_days) * int(rigging_artists) * float(rigging_salary)) +
                        ((float(rigging_salary) / total_salary) * overhead)) * ((100+profit_margin)/100)
        else:
            rigging_price = 0.00

        if int(lookdev_artists) != 0 and int(lookdev_days) != 0:
            lookdev_price = ((int(lookdev_days) * int(lookdev_artists) * float(lookdev_salary)) +
                        ((float(lookdev_salary) / total_salary) * overhead)) * ((100+profit_margin)/100)
        else:
            lookdev_price = 0.00

        if int(fx_artists) != 0 and int(fx_days) != 0:
            fx_price = ((int(fx_days) * int(fx_artists) * float(fx_salary)) +
                    ((float(fx_salary) / total_salary) * overhead)) * ((100+profit_margin)/100)
        else:
            fx_price = 0.00
        
        if int(modelling_artists) != 0 and int(modelling_days) != 0:
            modelling_price = ((int(modelling_days) * int(modelling_artists) * float(modelling_salary)) +
                            ((float(modelling_salary) / total_salary) * overhead)) * ((100+profit_margin)/100)
        else:
            modelling_price = 0.00

        if int(layout_artists) != 0 and int(layout_days) != 0:
            layout_price = ((int(layout_days) * int(layout_artists) * float(layout_salary)) +
                            ((float(layout_salary) / total_salary) * overhead)) * ((100+profit_margin)/100)
        else:
            layout_price = 0.00

        if int(lighting_artists) != 0 and int(lighting_days) != 0:
            lighting_price = ((int(lighting_days) * int(lighting_artists) * float(lighting_salary)) +
                            ((float(lighting_salary) / total_salary) * overhead)) * ((100+profit_margin)/100)
        else:
            lighting_price = 0.00

        if int(rendering_artists) != 0 and int(rendering_days) != 0:
            rendering_price = ((int(rendering_days) * int(rendering_artists) * float(rendering_salary)) +
                            ((float(rendering_salary) / total_salary) * overhead)) * ((100+profit_margin)/100)
        else:
            rendering_price = 0.00

        #Voice Stage
        if int(audio_studio_artists) != 0 and int(audio_studio_days) != 0:
            audio_studio_price = ((int(audio_studio_days) * int(audio_studio_artists) * float(audio_studio_salary)) +
                                ((float(audio_studio_salary) / total_salary) * overhead)) * ((100+profit_margin)/100)
        else:
            audio_studio_price = 0.00

        if int(music_sync_artists) != 0 and int(music_sync_days) != 0:
            music_sync_price = ((int(music_sync_days) * int(music_sync_artists) * float(music_sync_salary)) +
                                ((float(music_sync_salary) / total_salary) * overhead)) * ((100+profit_margin)/100)
        else:
            music_sync_price = 0.00

        if int(voiceover_salary) > 0:
            voiceover_price = (float(voiceover_salary)*1.25*1.2)
        else:
            voiceover_price = 0.00
        
        

        total_sum = (moodboard_price + illustration_price + storyboard_price +
             compositing_price + editing_price + motion_price +
             texturing_price + animation_price + rigging_price +
             lookdev_price + fx_price + modelling_price + layout_price +
             lighting_price + rendering_price + voiceover_price +
             audio_studio_price + music_sync_price)
        prod_mgt = 0.05*total_sum

        if float(vat) > 1:
            vat_price = (total_sum + prod_mgt)*0.075
        else:
            vat_price = 0.00

        
        total_sum = total_sum + prod_mgt
        final_cost = total_sum + vat_price

        

        context = {
            'moodboard_price': moodboard_price,
            'illustration_price': illustration_price,
            'storyboard_price': storyboard_price,
            'compositing_price': compositing_price,
            'editing_price': editing_price,
            'motion_price': motion_price,
            'texturing_price': texturing_price,
            'animation_price': animation_price,
            'rigging_price': rigging_price,
            'lookdev_price': lookdev_price,
            'fx_price': fx_price,
            'modelling_price': modelling_price,
            'layout_price': layout_price,
            'lighting_price': lighting_price,
            'rendering_price': rendering_price,
            'voiceover_price': voiceover_price,
            'audio_studio_price': audio_studio_price,
            'music_sync_price': music_sync_price,
            'total_sum': total_sum,
            'prod_mgt': prod_mgt,
            'final_cost': final_cost,
            'vat_price': vat_price,
            'invoice_id': invoice_id,
            'company_name': company_name,
            'invoice_title': invoice_title,
            'company_location': company_location,
            'moodboard': moodboard,
            'motion': motion,
            'modelling': modelling,
            'texturing': texturing,
            'rigging': rigging,
            'animation': animation,
            'fx': fx,
            'lighting': lighting,
            'voiceover': voiceover,
            'music_sync': music_sync,
            'audio_studio': audio_studio,
            'layout': layout,
            'lookdev': lookdev,
            'storyboard': storyboard,
            'illustration': illustration,
            'compositing': compositing,
            
        }

        
        
        
        return render(request, 'summary.html', context)
    
def invoice_summary(request):
    if request.method == 'POST':
        details = PriceDetail(
            company_name = request.POST.get('company_name'),
            invoice_id = request.POST.get('invoice_id'),
            invoice_title = request.POST.get('invoice_title'),
            company_location = request.POST.get('company_location'),
            moodboard_price=request.POST.get('moodboard_price'),
            illustration_price=request.POST.get('illustration_price'),
            storyboard_price=request.POST.get('storyboard_price'),
            compositing_price=request.POST.get('compositing_price'),
            editing_price=request.POST.get('editing_price'),
            motion_price=request.POST.get('motion_price'),
            modelling_price=request.POST.get('modelling_price'),
            texturing_price=request.POST.get('texturing_price'),
            rigging_price=request.POST.get('rigging_price'),
            lookdev_price=request.POST.get('lookdev_price'),
            layout_price=request.POST.get('layout_price'),
            animation_price=request.POST.get('animation_price'),
            fx_price=request.POST.get('fx_price'),
            lighting_price=request.POST.get('lighting_price'),
            rendering_price=request.POST.get('rendering_price'),
            audio_studio_price=request.POST.get('audio_studio_price'),
            music_sync_price=request.POST.get('music_sync_price'),
            voiceover_price=request.POST.get('voiceover_price'),
            total_sum=request.POST.get('total_sum'),
            vat_price=request.POST.get('vat_price'),
            prod_mgt=request.POST.get('prod_mgt'),
            final_cost=request.POST.get('final_cost'),               
        )
        details.save()
        includes = PriceInclude(
            moodboard = bool(request.POST.get('moodboard')),
            motion = bool(request.POST.get('motion')),
            modelling = bool(request.POST.get('modelling')),
            texturing = bool(request.POST.get('texturing')),
            rigging = bool(request.POST.get('rigging')),
            animation = bool(request.POST.get('animation')),
            fx = bool(request.POST.get('fx')),
            lighting = bool(request.POST.get('lighting')),
            voiceover = bool(request.POST.get('voiceover')),
            music_sync = bool(request.POST.get('music_sync')),
            audio_studio = bool(request.POST.get('audio_studio')),
            layout = bool(request.POST.get('layout')),
            lookdev = bool(request.POST.get('lookdev')),
            illustration = bool(request.POST.get('illustration')),
            storyboard = bool(request.POST.get('storyboard')),
            compositing = bool(request.POST.get('compositing')),
            price_detail = PriceDetail.objects.get(pk=details.id)
        )

        includes.save()
        return redirect(f'/invoices/{details.id}')
    

def invoice(request, pk):
    data = PriceDetail.objects.get(pk=pk)
    include_data = PriceInclude.objects.get(price_detail=pk)
    cost_in_words = num2words(round(float(data.final_cost)))
    context = {'data': data, 
               'include_data': include_data, 
               'cost_in_words': cost_in_words}
    return render(request, 'gen_invoice.html', context)
  

"""
def gen_invoice(request, pk):


    pdf = pdfkit.from_url(request.build_absolute_uri(reverse("accounts:invoices", kwargs={'pk': pk})), False, configuration=config)

    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename=file_name.pdf'
    return response"""




def success(request):
   
    return render(request, 'success.html')



def settings(request):
    salaries = Salaries.objects.all()
    return render(request, 'settings.html', {'salaries': salaries})