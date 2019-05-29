from django import forms

class ProductInsertForm(forms.Form):
    product_id=forms.IntegerField(
        label="Enter your product id",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'your product id',
            }
        )
    )
    product_name=forms.CharField(
        label="Enter your product name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'your product name'
            }
        )
    )
    product_cost=forms.IntegerField(
        label="Enter your product cost",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'your product cost'
            }
        )
    )
    product_color = forms.CharField(
        label="Enter your product color",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your product color'
            }
        )
    )
    product_class = forms.CharField(
        label="Enter your product class",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your product class'
            }
        )
    )
    customer_name = forms.CharField(
        label="Enter your name",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your customer name'
            }
        )
    )
    customer_mobile = forms.IntegerField(
        label="Enter your customer mobile",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your customer mobile'
            }
        )
    )
    customer_email = forms.EmailField(
        label="Enter your email id",
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your email id'
            }
        )
    )
class ProductUpdateForm(forms.Form):
    product_id = forms.IntegerField(
        label="Enter your product id",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your product id'
            }
        )
    )


    product_cost = forms.IntegerField(
        label="Enter your product cost",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your product cost'
            }
        )
    )
class ProductDeleteForm(forms.Form):
    product_id = forms.IntegerField(
        label="Enter your product id",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your product id'
            }
        )
    )
