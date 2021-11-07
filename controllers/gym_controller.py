from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.gym import Gym
import repositories.gym_repository as gym_repository
import repositories.member_repository as member_repository
import repositories.session_repository as session_repository

gyms_blueprint = Blueprint("gyms", __name__)



