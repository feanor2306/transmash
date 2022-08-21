from abc import ABC
from django.forms import models
from rest_framework import serializers
from .models import Skills, Branches, Personal, Employee
from rest_framework.renderers import JSONRenderer


# class EmployeeModel:
#  def __init__(self, name, seniority):
#    self.name = name
#  self.seniority = seniority
#

class BranchesSerializer(serializers.ModelSerializer):
    class Meta:
        model: Branches
        fields = "__all__"


class PersonalSerializer(serializers.ModelSerializer):
    class Meta:
        model: Personal
        fields = "__all__"


class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = "__all__"


class EmployeeSerializer(serializers.ModelSerializer):
    skills_level = SkillsSerializer(many=True, required=False)
    photo = serializers.ImageField(required=False)

    class Meta:
        model = Employee
        fields = "__all__"

    def create(self, validated_data):
        skills_level = validated_data.pop("skills_level", None)
        skills_instances = []
        if skills_level is not None:
            # for skill in skills_level:
            #     skills_id = skill.get("id", None)
            #     if skills_id:
            #         try:
            #             skills_instance = Skills.objects.get(id=skills_id)
            #             skills_instance.name = skill.name
            #             skills_instance.grade = skill.grade
            #             skills_instance.save()
            #             skills_level.pop(skill)
            #         except Skills.DoesNotExist:
            #             raise ValueError("Такого id не найдено")
            skills_level_serializer = SkillsSerializer(data=skills_level, many=True)
            skills_level_serializer.is_valid(raise_exception=True)
            skills_instances = skills_level_serializer.save()
        instance = Employee.objects.create(**validated_data)
        for skill in skills_instances:
            instance.skills_level.add(skill)
        instance.save()

        return instance
    # name = serializers.CharField(max_length=255)
    # photo = serializers.ImageField(read_only=True)
    # photo_upload = serializers.CharField(write_only=True, required=False)

    # cat = serializers.CharField(read_only=True)
    # explored_branches = BranchesSerializer(read_only=True)  # Выбираются все шахты, на которых сотрудник работал 2 недели и более
    # favorite_branch = BranchesSerializer(read_only=True)  # Выбирается одна шахта
    # skills_level = SkillsSerializer(required=False, allow_null=True)
    # personal_qualities = PersonalSerializer(read_only=True)
    # medical = serializers.CharField(read_only=True)
    # special = serializers.CharField(read_only=True)

    # class Meta:
    #    model: Employee
    #    fields = "__all__"

    # def create(self, validated_data):
    #   return Employee.objects.create(**validated_data)
    #   #skills = validated_data.pop("skills", None)
    #   #logo_upload = validated_data.pop("logo_upload", None)
    #  #address = validated_data.pop("address_id", None)
    #  #organizational_legal_form = validated_data.pop("organizational_legal_form", None)
    # bank_details = validated_data.pop("bank_details", None)

    # def update(self, instance, validated_data):
    #   instance.name = validated_data.get('name', instance.name)
    #  instance.seniority = validated_data.get('seniority', instance.seniority)
    # instance.cat = validated_data.get('cat', instance.cat)
    # instance.explored_branches = validated_data.get('explored_branches', instance.explored_branches)
    # instance.favorite_branch = validated_data.get('favorite_branch', instance.favorite_branch)
    # #instance.skills_level = validated_data.get('skills_level', instance.skills_level)
    # instance.personal_qualities = validated_data.get('personal_qualities', instance.personal_qualities)
    # instance.medical = validated_data.get('medical', instance.medical)
    # instance.special = validated_data.get('special', instance.special)
    # instance.save()
    # return instance

    # def delete(self, instance):

    # if logo_upload is not None:
    #  try:
    #   _logo_file = get_img_from_data_url(logo_upload)[0]
    # except Exception:
    #  raise serializers.ValidationError(_('Not valid media "image".'))

    # validated_data["logo"] = _logo_file

# def validate(self, attrs):
# return attrs


# def encode():
#   model = EmployeeModel('Rodichkin Andrey', 'Seniority: Ingineer')
#  model_sr = EmployeeSerializer(model)
# json = JSONRender().render(model_sr.data)
# print(json)
