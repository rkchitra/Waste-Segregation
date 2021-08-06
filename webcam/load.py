from fastai.vision import *

def predict_waste(filename) :
	path = 'C:/Users/chitr/Desktop/Integrate_Modules'
	learn = load_learner(path,'export.pkl')
	print("Loaded model successfully!")
	biodegradable = ['Tea_bags_128','cardboard_128','deg_bags_128','kwaste_128','woodleaves_128','paper_128']
	mapping = dict.fromkeys(biodegradable, 'biodegradable')
	nonbio = ['cans_128','glass_128','gthermocol_128','masks_128','pen_128','plastic_128','plasticfoodbox_128','Straw_128','Wrappers_128']

	for x in nonbio :
		mapping.update({x:'nonbiodegradable'})
	#print("dictionary: ",mapping)
	pred_class,pred_idx,outputs = learn.predict(open_image(filename))
	#b_nb = mapping[str(pred_class)] 
	b_nb = ''
	if str(pred_class) in biodegradable :
		b_nb = 'biodegradable'
	else :
	 	b_nb = 'nonbiodegradable'
	ret = str(pred_class) + "("+b_nb + ")"
	print(ret)
	return b_nb