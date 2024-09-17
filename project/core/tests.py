from django.test import TestCase

# Create your tests here.


# <navbar style="display: flex; justify-content: center;">
#     <button><a href="{% url 'core:index' %}">Home</a></button>
#     {% if user.is_authenticated %}
#         <button><a href="{% url 'core:profile' %}">{{ user.username }}</a></button>
#         {% if user.usuario.avatar %}
#         <img src="{{ user.usuario.avatar.url }}" alt="avatar" style="height: 30px;" >
#         {% else %}
#         <img src="{% static 'core/img/usuario.png' %}" alt="avatar" style="height: 30px;" >
#     {% endif %}
#         <form action="{% url 'core:logout' %}" method="post">
#             {% csrf_token %}
#             <button type="submit">Logout</button>
#         </form>
#         <button><a href="{% url 'usuarios:index' %}">Usuarios</a></button>
#         <button><a href="{% url 'autos:index' %}">Autos</a></button>    
#     {% else %}    
#         <button><a href="{% url 'core:login' %}">Login</a></button>
#     {% endif %}
# </navbar>
