from django.contrib import admin
from catalog.models import Author, Genre, Book, BookInstance

# admin.site.register(Book)
# admin.site.register(Author)
admin.site.register(Genre)
# admin.site.register(BookInstance)


# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]


# below code will add the Book information inline to our Author detail. Please comment above three lines of code 
    
# class BooksInline(admin.TabularInline):
#     model = Book

# # Define the admin class
# class AuthorAdmin(admin.ModelAdmin):
#     list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
#     fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
#     inlines = [BooksInline]

# Register the admin class with associated model
admin.site.register(Author, AuthorAdmin)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')

# below code will add the BookInstance information inline to our Book detail. Please comment above three lines of code 

# class BooksInstanceInline(admin.TabularInline):
#     model = BookInstance

# # Register the Admin classes for Book using the decorator
# @admin.register(Book)
# class BookAdmin(admin.ModelAdmin):
#     list_display = ('title', 'author', 'display_genre')
#     inlines = [BooksInstanceInline]


# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'due_back', 'id')
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )