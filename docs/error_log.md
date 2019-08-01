Terminal:      django.template.exceptions.TemplateDoesNotExist: courses/course_list.html
                (similar situation with memberships/profile was dealt with by removing memberships)
Browser:       TemplateDoesNotExist at /   courses/course_list.html
Solution:      in settings of your project, under Templates, edit DIRS to include templates


Terminal:      error: pathspec 'change'' did not match any file(s) known to git.
Solution:      ???


Go to https://getbootstrap.com/docs/3.3/getting-started/ to get the correct Bootstrap CDN  


Terminal:       django.template.exceptions.TemplateSyntaxError: Invalid block tag on line 19: 'csrf', expected
                'elif', 'else' or 'endif'. Did you forget to register or load this tag?
Browser:        TemplateSyntaxError at /memberships/
                Invalid block tag on line 19: 'csrf', expected 'elif', 'else' or 'endif'. Did you forget to register or load this tag?
Solution:       my syntax was wrong


Terminal:           selected_membership = request.post.get('membership_type')
                    AttributeError: 'WSGIRequest' object has no attribute 'post'
Solution:           post in membership_list.html might be in lower-case, in views it must be upper



Terminal:       AttributeError: 'str' object has no attribute 'get'
Solution:       


Terminal: 
                 ERRORS:
                 ?: (staticfiles.E002) The STATICFILES_DIRS setting should not contain the STATIC_ROOT setting.
Solution:          STATIC_ROOT = os.path.join(BASE_DIR, 'static_root/'), changed it to just static



Terminal:       django.template.exceptions.TemplateSyntaxError: Invalid block tag on line 24: 'static_root', e
                xpected 'endblock'. Did you forget to register or load this tag?
Browser:        TemplateSyntaxError at /memberships/payment
                Invalid block tag on line 24: 'static_root', expected 'endblock'. Did you forget to register or load this tag?
                
Solution:       changed  <!-- <script src="{% static_root 'js/stripeV3.js' %}"></script> --> to just static


Terminal:           if user_membership.membership == selected_membership:
                    UnboundLocalError: local variable 'selected_membership' referenced before assignment
Solution:       


Terminal:        except stripe.CardError as e:
                 AttributeError: module 'stripe' has no attribute 'CardError'
Solution:        installed correct version, removed source=token from views