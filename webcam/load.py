from fastai.vision import *

def predict_waste(filename) :
	path = 'C:/Users/chitr/Desktop/Integrate_Modules'
	learn = load_learner(path,'export.pkl')
	biodegradable = ['Tea_bags_128','cardboard_128','deg_bags_128','kwaste_128','woodleaves_128']
	print("Loaded model successfully!")
	pred_class,pred_idx,outputs = learn.predict(open_image(filename))
	b_nb = '' 
	if str(pred_class) in biodegradable :
		b_nb = 'biodegradable'
	else :
	 	b_nb = 'nonbiodegradable'
	ret = str(pred_class) + "("+b_nb + ")"
	return ret