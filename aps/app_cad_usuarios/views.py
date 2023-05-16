from django.shortcuts import render, redirect
from .models import Usuario

def home(request):
    return render(request, 'usuarios/home.html')

def usuarios(request):
    #Salvando no banco
    if request.method == 'POST':
        novo_usuario = Usuario()
        novo_usuario.nome = request.POST.get('nome')
        novo_usuario.idade = request.POST.get('idade')
        novo_usuario.save()

    #exibir os usuarios já cadastrados
    # dicionario
    usuarios = {
        'usuarios' : Usuario.objects.all()
    }

    #retornar para a pagina de listagem
    return render(request, 'usuarios/usuarios.html', usuarios)




def deletar(request):
    if request.method == 'POST':
        id_usuario = request.POST.get('id_usuario')
        Usuario.objects.filter(id=id_usuario).delete()
        return redirect('listagem_usuarios')

    return render(request, 'usuarios/usuarios.html')



'''def deletar(request):
    if request.method == 'POST':
        id_usuario = request.POST.get('id_usuario')
        try:
            usuario = Usuario.objects.get(id=id_usuario)
            usuario.delete()
        except Usuario.DoesNotExist:
            pass
        return redirect('listagem_usuarios')

    return render(request, 'usuarios/usuarios.html')'''




'''def deletar(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')
        if (Usuario.objects.filter(nome) == nome) and (Usuario.objects.filter(idade) == idade):
            Usuario.objects.filter(nome).delete()
            Usuario.objects.filter(idade).delete()
        return redirect('listagem_usuarios')

    return render(request, 'usuarios/usuarios.html')'''


'''def deletar (request):
    id = request.POST.get('id_usuario')
    for usuario in Usuario.objects.all():
        if str(id) == usuario.id_usuario:
            usuario.delete()

    usuarios = {
        'usuarios' : Usuario.objects.all()
    }
    return render(request, 'usuarios/usuarios.html', usuarios)'''
