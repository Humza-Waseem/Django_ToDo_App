1.################## Commit (user specification & Mixin) : I added the functionality in which every user will see only the content which is related  to them.   like  the 

#! def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['tasks'] = context['tasks'].filter(user=self.request.user) # this allows us to filter the tasks based on the user that is logged in. This will only show the tasks that are created by the user that is logged in

#        # context['count'] = context['tasks'].filter(complete = False).count() # this will count the number of tasks that are not completed
#         return context

#*  It filters the tasks based on the user and returns the context data. The function is used in a class-based view to provide the context data to the template. This helps in customizing the data based on the user's request and providing a personalized experience.


2.##################  Then I added the functionality in the logout button and made it a form so that i could add the csrf token to it., then I added the functionality to redirect the user to the login page after logging out by setting the loginRequiredMixin in the taskList view.


   