import time
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import cross_validate, cross_val_predict


def plot_regression_results(ax, y_true, y_pred, title, scores, elapsed_time):
    """Scatter plot of the predicted vs true targets.
    """
    ax.plot([y_true.min(), y_true.max()],
            [y_true.min(), y_true.max()],
            '--r', linewidth=2)
    ax.scatter(y_true, y_pred, alpha=0.2)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    ax.spines['left'].set_position(('outward', 10))
    ax.spines['bottom'].set_position(('outward', 10))
    ax.set_xlim([y_true.min(), y_true.max()])
    ax.set_ylim([y_true.min(), y_true.max()])
    ax.set_xlabel('Measured')
    ax.set_ylabel('Predicted')
    extra = plt.Rectangle((0, 0), 0, 0, fc="w", fill=False,
                          edgecolor='none', linewidth=0)
    ax.legend([extra], [scores], loc='upper left')
    title = title + '\n Evaluation in {:.2f} seconds'.format(elapsed_time)
    ax.set_title(title)


def fit_cv_plot(X, y, axs, ests):
    """Fit X to y using provided estimators, and display results on provided axes.
    """
    outs = {}
    for ax, (name, est) in zip(axs, ests):
        start_time = time.time()
        outputs = cross_validate(est, X, y,
                                 return_estimator=True,
                                 groups=X.reset_index()['pin'],
                                 scoring=['r2', 'neg_mean_absolute_error'],
                                 n_jobs=-1, verbose=0)
        elapsed_time = time.time() - start_time

        y_pred = cross_val_predict(est, X, y, n_jobs=-1, verbose=0)
        plot_regression_results(ax, y, y_pred,name,
                                scores=(r'$R^2={:.2f} \pm {:.2f}$' + '\n' + r'$MAE={:.2f} \pm {:.2f}$')
                                .format(np.mean(outputs['test_r2']),
                                        np.std(outputs['test_r2']),
                                        -np.mean(outputs['test_neg_mean_absolute_error']),
                                        np.std(outputs['test_neg_mean_absolute_error'])),
                                elapsed_time=elapsed_time)

        outs[name] = outputs

    plt.suptitle('Ensemble predictors')
    plt.tight_layout()
    plt.subplots_adjust(top=0.85)
    plt.show()
    
    return outs