from django.shortcuts import render
from .models import Node
from .functions import add_node, edit_node, sort_all_nodes, get_parent, delete_node
from .forms import AddForms, EditForms, DeleteForms, SortForms
import plotly.express as px
import plotly.offline as opy


def graph_view(request):
    # Main view which present graph and all functionality

    add_form = AddForms()
    del_form = DeleteForms()
    edit_form = EditForms()
    sort_form = SortForms(request.GET or None)

    root_set = Node.objects.all()

    if request.method == 'GET':
        if request.GET.__contains__('name_add'):

            add_form = AddForms(request.GET)
            if add_form.is_valid():
                name = add_form.cleaned_data['name_add']
                value = add_form.cleaned_data['value_add']

                add_node(name, value)

        elif request.GET.__contains__('name_delete'):
            del_form = DeleteForms(request.GET)
            if del_form.is_valid():
                del_node = del_form.cleaned_data['name_delete']
                delete_node(del_node.id)

        elif request.GET.__contains__('id_edit'):
            edit_form = EditForms(request.GET)
            if edit_form.is_valid():

                name = edit_form.cleaned_data['name_edit']
                value = edit_form.cleaned_data['value_edit']
                id = edit_form.cleaned_data['id_edit'].id

                edit_node(name, value, id)

        elif request.GET.__contains__('sort_all'):
            if sort_form.is_valid():
                sort_all = sort_form.cleaned_data['sort_all']
                if sort_all:
                    sort_all_nodes(root_set)

    query = Node.objects.all()
    names, parents = get_parent(query)

    if query:
        fig = px.treemap(
            names=names,
            parents=parents,
        )

        div = opy.plot(fig, auto_open=False, output_type='div')
    else:
        div = None

    context = {
        'graph': div,
        'add_form': add_form,
        'edit_form': edit_form,
        'del_form': del_form,
        'sort_form': sort_form
    }

    return render(request, 'home.html', context)
