def add_decorator(func):
    def wrapper(*args):
        print(f"'{func.__name__}' is running, with args {args}")
        result=func(*args)
        print(f"'{func.__name__}' has completed")
        return result
    return wrapper
@add_decorator
def add(a, b):
    return a+b
print( "Addition of given numbers are:", add(4,5))

# def this_decorator(func):
# 	def wrapper(*args):
# 		print(f"'{func.__name__}' Function is running now")
# 		result = func(*args)
# 		print(f"'{func.__name__}'Function has completed working")
# 		return result
# 	return wrapper
# @this_decorator
# def greet(a):
# 	return a
# print(f"Hello", greet("Ruchitha"), "How are you?")

# import time
# def timing_decorator(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         end = time.time()
#         print(f"{func.__name__} took {end - start:.2f} seconds to run.")
#         return result
#     return wrapper

# @timing_decorator
# def deploy_app():
#     print("Deploying application...")
#     time.sleep(5)  # simulate time delay
#     print("Deployment complete!")

# deploy_app()
