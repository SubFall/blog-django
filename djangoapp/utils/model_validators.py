from django.core.exceptions import ValidationError

def validate_png(imagem):
    if not imagem.name.lower().endswith('.png'):
        raise ValidationError('A imagem deve estar no formato PNG')