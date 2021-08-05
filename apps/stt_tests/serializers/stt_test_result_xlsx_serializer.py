from rest_framework import serializers

from apps.stt_tests.models import SttTestResult


class SttTestResultXlsxSerializer(serializers.ModelSerializer):
    language = serializers.CharField(source='stt_test.language.code')
    text = serializers.SerializerMethodField()
    characters_count = serializers.SerializerMethodField()
    characters_count_excluding_whitespace = serializers.SerializerMethodField()
    words_count = serializers.SerializerMethodField()
    age = serializers.IntegerField(source='user.age')
    formatted_result = serializers.SerializerMethodField()
    edit_distance = serializers.SerializerMethodField()
    similarity = serializers.SerializerMethodField()
    difference = serializers.SerializerMethodField()

    class Meta:
        model = SttTestResult
        fields = ['language', 'text', 'characters_count', 'characters_count_excluding_whitespace', 'words_count', 'age',
                  'result', 'formatted_result', 'edit_distance', 'similarity', 'difference']

    def get_text(self, obj):
        return obj.stt_test.text.lower()

    def get_characters_count(self, obj):
        text = obj.stt_test.text
        return len(text)

    def get_characters_count_excluding_whitespace(self, obj):
        text = obj.stt_test.text
        return len(text) - text.count(' ')

    def get_words_count(self, obj):
        return len(obj.stt_test.text.split())

    def get_formatted_result(self, obj):
        return obj.result.lower()

    def get_edit_distance(self, obj):
        text = obj.stt_test.text.lower()
        result = obj.result.lower()
        return self._levenshtein(text, result)

    def get_similarity(self, obj):
        text = obj.stt_test.text.lower()
        result = obj.result.lower()
        edit_distance = self._levenshtein(text, result)
        return 1 - min(float(edit_distance) / float(len(text)), 1.0)

    def get_difference(self, obj):
        text = obj.stt_test.text.lower()
        result = obj.result.lower()
        edit_distance = self._levenshtein(text, result)
        return float(edit_distance) / float(len(text))

    @classmethod
    def _levenshtein(cls, s1, s2):
        """Source: https://en.wikibooks.org/wiki/Algorithm_Implementation/Strings/Levenshtein_distance"""
        if len(s1) < len(s2):
            return cls._levenshtein(s2, s1)
        if len(s2) == 0:
            return len(s1)

        previous_row = range(len(s2) + 1)
        for i, c1 in enumerate(s1):
            current_row = [i + 1]
            for j, c2 in enumerate(s2):
                insertions = previous_row[j + 1] + 1
                deletions = current_row[j] + 1
                substitutions = previous_row[j] + (c1 != c2)
                current_row.append(min(insertions, deletions, substitutions))
            previous_row = current_row

        return previous_row[-1]
