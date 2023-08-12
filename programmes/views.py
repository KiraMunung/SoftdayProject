from django.shortcuts import render
from .models import *
from django.views.generic import DetailView, ListView, DeleteView, UpdateView, CreateView, FormView
from .form import LeconForm, ComForm, RepForm
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy


class NiveauListView(ListView):
    context_object_name = 'niveaux'
    model = Niveaux
    template_name = 'programmes/niveaulist.html'


class MatiereListView(DetailView):
    context_object_name = 'niveau'
    model = Niveaux
    template_name = 'programmes/matierelist.html'


class LeconListView(DetailView):
    context_object_name = 'matieres'
    model = Matiere
    template_name = 'programmes/leconlist.html'

class LeconListViewDetail(DetailView, FormView):
    context_object_name = 'lecon'
    model = Lecon
    template_name = 'programmes/leconlistdetail.html'

    form_class = ComForm
    second_form_class = RepForm

    def get_context_data(self, **kwargs):
        context = super(LeconListViewDetail, self).get_context_data(**kwargs)

        if 'form' not in context:
            context['form']=self.form_class()

        if 'form2' not in context:
            context['form2']=self.second_form_class()

        return context



    def get_success_url(self):
        self.object = self.get_object()
        niveau = self.object.niveau
        matiere = self.object.matiere
        return reverse_lazy('programmes:leconlistdetail', kwargs={
            'niveau':niveau,
            'matiere':matiere,
            'slug':self.object.slug
        })


    def form_valid(self, form):
            self.object = self.get_object()
            fd = form.save(commit=False)
            fd.auteur = self.request.user
            #fd.lesson = self.object.comments.nom
            fd.nom_lesson_id = self.object.id
            fd.save()
            return HttpResponseRedirect(self.get_success_url())

    def form_valid2(self, form):
        self.object = self.get_object()
        fd = form.save(commit=False)
        fd.auteur = self.request.user
        fd.nom_comm_id = self.request.POST.get('comment_id')
        fd.save()
        return HttpResponseRedirect(self.get_success_url())





    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if 'form' in request.POST:
            form_class = self.form_class

            form_name = 'form'

        else:
            form_class= self.second_form_class
            form_name = 'form2'
        form = self.get_form(form_class)

        if form_name=='form' and form.is_valid():
            print('nouveau commentaire')
            return self.form_valid(form)

        if form_name=='form2' and form.is_valid():
            print('nouvelle reponse')
            return self.form_valid2(form)


        



        

        
    



class LeconCreateView(CreateView):
    form_class = LeconForm
    context_object_name = 'matieres'
    model = Matiere
    template_name = 'programmes/leconcreate.html'

    def get_success_url(self):
        self.object = self.get_object()
        niveau = self.object.niveau
        return reverse_lazy('programmes:leconlist', kwargs={'niveau':niveau, 'slug':self.object.slug})


    def form_valid(self, form, *args, **kwargs):
        self.object = self.get_object()
        ls = form.save(commit=False)
        ls.creer_par = self.request.user
        ls.niveau = self.object.niveau
        ls.matiere = self.object
        ls.save()
        return HttpResponseRedirect(self.get_success_url())


class LeconUpdateView(UpdateView):
    fields = ('nom', 'position', 'pdf', 'fpe')
    context_object_name = 'lecon'
    model = Lecon
    template_name = 'programmes/leconupdate.html'


class LeconDeleteView(DeleteView):
    model= Lecon
    context_object_name = "lecon"
    template_name= 'programmes/lecondelete.html'

    def get_success_url(self):
        niveau = self.object.niveau
        matiere = self.object.matiere
        return reverse_lazy("programmes:leconlist", kwargs={'niveau':niveau, 'slug':matiere.slug})