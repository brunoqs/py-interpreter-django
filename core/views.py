from django.shortcuts import render
import subprocess

# Create your views here.

def index(request):
	output = ''
	if request.method == 'POST':
		code = request.POST.get('code')
		f = open('file.py', 'w+')
		f.write(str(code))
		output = subprocess.check_output("python /home/unclear/Projetos/pyweb/file.py", stderr=subprocess.STDOUT, shell=True)
		context = {'code': output}
		print (output.decode("utf-8"))
		return render(request, "core/index.html", context)
	else:
		return render(request, "core/index.html", {})
