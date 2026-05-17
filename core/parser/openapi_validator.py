import json
import yaml

class OpenAPIValidator:

    REQUIRED_KEYS = [
        'paths'
    ]

    SIGNATURE_KEYS = [
        'openapi',
        'swagger'
    ]

    @staticmethod
    def validate(content, content_type=''):

        parsed = None

        try:
            if 'json' in content_type.lower():
                parsed = json.loads(content)
            else:
                parsed = yaml.safe_load(content)

        except Exception:
            return {
                'valid': False,
                'confidence': 0,
                'reason': 'parse_failed'
            }

        if not isinstance(parsed, dict):
            return {
                'valid': False,
                'confidence': 0,
                'reason': 'not_dictionary'
            }

        has_signature = any(
            key in parsed for key in OpenAPIValidator.SIGNATURE_KEYS
        )

        has_required = all(
            key in parsed for key in OpenAPIValidator.REQUIRED_KEYS
        )

        confidence = 0

        if has_signature:
            confidence += 60

        if has_required:
            confidence += 40

        return {
            'valid': confidence >= 80,
            'confidence': confidence,
            'reason': 'validated'
        }
