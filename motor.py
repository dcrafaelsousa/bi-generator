Feedback Type:
Frown (Error)

Timestamp:
2026-04-17T02:42:41.2020602Z

Local Time:
2026-04-16T21:42:41.2020602-05:00

Session ID:
a94580c9-4e8c-498f-917a-17762f01802c

Release:
March 2026

Product Version:
2.152.1279.0 (26.03)+7cb753613ff9dbf770467b6b4012425246d1fe94 (x64)

Error Message:
Expected 'artifacts' array containing 'report' artifact with valid 'path' property in 'C:\Users\Rafael\AppData\Local\Temp\27ec8b8d-f0b3-4965-8b42-a11562e79076_proyecto_pbip (4).zip.076\proyecto.pbip'.

Stack Trace:
   en Microsoft.PowerBI.Client.Windows.Services.BiProjectOperationHandler.<WithProjectExceptionConversion>d__51`1.MoveNext()
--- Fin del seguimiento de la pila de la ubicación anterior donde se produjo la excepción ---
   en System.Runtime.ExceptionServices.ExceptionDispatchInfo.Throw()
   en System.Runtime.CompilerServices.TaskAwaiter.HandleNonSuccessAndDebuggerNotification(Task task)
   en Microsoft.PowerBI.Client.Windows.Services.BiProjectOperationHandler.<>c__DisplayClass46_0.<<LoadFromPbip>g__LoadFromPbipCore|0>d.MoveNext()
--- Fin del seguimiento de la pila de la ubicación anterior donde se produjo la excepción ---
   en System.Runtime.ExceptionServices.ExceptionDispatchInfo.Throw()
   en System.Runtime.CompilerServices.TaskAwaiter.HandleNonSuccessAndDebuggerNotification(Task task)
   en Microsoft.PowerBI.Client.Windows.Telemetry.PowerBITelemetryServiceExtensions.<EmitStandardizedClientReportingEventWithDebugEvent>d__7`1.MoveNext()
--- Fin del seguimiento de la pila de la ubicación anterior donde se produjo la excepción ---
   en System.Runtime.ExceptionServices.ExceptionDispatchInfo.Throw()
   en System.Runtime.CompilerServices.TaskAwaiter.HandleNonSuccessAndDebuggerNotification(Task task)
   en Microsoft.PowerBI.Client.Windows.Services.BiProjectOperationHandler.<EmitStandardizedClientReportingEventWithDebugEvent>d__48`1.MoveNext()
--- Fin del seguimiento de la pila de la ubicación anterior donde se produjo la excepción ---
   en System.Runtime.ExceptionServices.ExceptionDispatchInfo.Throw()
   en System.Runtime.CompilerServices.TaskAwaiter.HandleNonSuccessAndDebuggerNotification(Task task)
   en Microsoft.PowerBI.Client.Windows.Services.BiProjectOperationHandler.<LoadFromPbip>d__46.MoveNext()
--- Fin del seguimiento de la pila de la ubicación anterior donde se produjo la excepción ---
   en System.Runtime.ExceptionServices.ExceptionDispatchInfo.Throw()
   en System.Runtime.CompilerServices.TaskAwaiter.HandleNonSuccessAndDebuggerNotification(Task task)
   en Microsoft.PowerBI.Client.Windows.Services.BiProjectOperationHandler.<LoadArtifact>d__40.MoveNext()
--- Fin del seguimiento de la pila de la ubicación anterior donde se produjo la excepción ---
   en System.Runtime.ExceptionServices.ExceptionDispatchInfo.Throw()
   en System.Runtime.CompilerServices.TaskAwaiter.HandleNonSuccessAndDebuggerNotification(Task task)
   en Microsoft.PowerBI.Client.Windows.Services.CurrentArtifactManager.<>c__DisplayClass56_0.<<ExecuteAndHandleFileOpenErrors>b__0>d.MoveNext()
--- Fin del seguimiento de la pila de la ubicación anterior donde se produjo la excepción ---
   en System.Runtime.ExceptionServices.ExceptionDispatchInfo.Throw()
   en System.Runtime.CompilerServices.TaskAwaiter.HandleNonSuccessAndDebuggerNotification(Task task)
   en Microsoft.PowerBI.Client.Windows.Telemetry.PowerBITelemetryServiceExtensions.<EmitStandardizedClientReportingEventWithDebugEvent>d__7`1.MoveNext()
--- Fin del seguimiento de la pila de la ubicación anterior donde se produjo la excepción ---
   en System.Runtime.ExceptionServices.ExceptionDispatchInfo.Throw()
   en System.Runtime.CompilerServices.TaskAwaiter.HandleNonSuccessAndDebuggerNotification(Task task)
   en Microsoft.PowerBI.Client.Windows.Services.CurrentArtifactManager.<ExecuteAndHandleFileOpenErrors>d__56.MoveNext()
--- Fin del seguimiento de la pila de la ubicación anterior donde se produjo la excepción ---
   en System.Runtime.ExceptionServices.ExceptionDispatchInfo.Throw()
   en System.Runtime.CompilerServices.TaskAwaiter.HandleNonSuccessAndDebuggerNotification(Task task)
   en Microsoft.PowerBI.Client.Windows.Services.CurrentArtifactManager.<>c__DisplayClass37_0.<<OpenArtifactAndSetAsCurrent>b__0>d.MoveNext()
--- Fin del seguimiento de la pila de la ubicación anterior donde se produjo la excepción ---
   en System.Runtime.ExceptionServices.ExceptionDispatchInfo.Throw()
   en System.Runtime.CompilerServices.TaskAwaiter.HandleNonSuccessAndDebuggerNotification(Task task)
   en Microsoft.PowerBI.Client.Windows.Services.UIBlockingService.<>c__DisplayClass19_0`1.<<BlockUIAndRun>b__0>d.MoveNext()
--- Fin del seguimiento de la pila de la ubicación anterior donde se produjo la excepción ---
   en System.Runtime.ExceptionServices.ExceptionDispatchInfo.Throw()
   en Microsoft.PowerBI.Client.Windows.Services.UIBlockingService.WaitOnUIThreadForTaskCompletion[T](Task`1 task)
   en Microsoft.PowerBI.Client.Windows.Services.UIBlockingService.BlockUIAndRun[T](Func`1 asyncMethod, PowerBIProgress progress, String activityId)
   en Microsoft.PowerBI.Client.Windows.Services.CurrentArtifactManager.OpenArtifactAndSetAsCurrent(IPowerBIWindowService windowService, IPowerBIArtifact artifactToOpen, IExceptionHandler exceptionHandler, Nullable`1 entryPoint)
   en Microsoft.PowerBI.Client.CommandLineFileService.TryOpenOrCreateReport(IPowerBIWindowService windowService, IExceptionHandler exceptionHandler, Boolean forceCreate)
   en Microsoft.PowerBI.Client.AppReportFlow.<OpenExistingReport>d__50.MoveNext()
--- Fin del seguimiento de la pila de la ubicación anterior donde se produjo la excepción ---
   en System.Runtime.ExceptionServices.ExceptionDispatchInfo.Throw()
   en Microsoft.PowerBI.Client.AppReportFlow.<OpenExistingReport>d__50.MoveNext()
--- Fin del seguimiento de la pila de la ubicación anterior donde se produjo la excepción ---
   en System.Runtime.ExceptionServices.ExceptionDispatchInfo.Throw()
   en System.Runtime.CompilerServices.TaskAwaiter.HandleNonSuccessAndDebuggerNotification(Task task)
   en Microsoft.PowerBI.Client.AppReportFlow.<ContinueLoadWithMainWindow>d__43.MoveNext()
--- Fin del seguimiento de la pila de la ubicación anterior donde se produjo la excepción ---
   en System.Runtime.ExceptionServices.ExceptionDispatchInfo.Throw()
   en System.Runtime.CompilerServices.TaskAwaiter.HandleNonSuccessAndDebuggerNotification(Task task)
   en Microsoft.PowerBI.Client.AppModule.<>c__DisplayClass4_2.<<Run>b__4>d.MoveNext()
--- Fin del seguimiento de la pila de la ubicación anterior donde se produjo la excepción ---
   en System.Runtime.ExceptionServices.ExceptionDispatchInfo.Throw()
   en System.Runtime.CompilerServices.TaskAwaiter.HandleNonSuccessAndDebuggerNotification(Task task)
   en Microsoft.PowerBI.Client.Windows.MainWindow.<<ActivateMainWindow>b__41_1>d.MoveNext()
--- Fin del seguimiento de la pila de la ubicación anterior donde se produjo la excepción ---
   en System.Runtime.ExceptionServices.ExceptionDispatchInfo.Throw()
   en System.Runtime.CompilerServices.TaskAwaiter.HandleNonSuccessAndDebuggerNotification(Task task)
   en Microsoft.PowerBI.Client.Windows.IExceptionHandlerExtensions.<HandleAwaitableAsyncExceptions>d__1.MoveNext()

Stack Trace Message:
Expected 'artifacts' array containing 'report' artifact with valid 'path' property in 'C:\Users\Rafael\AppData\Local\Temp\27ec8b8d-f0b3-4965-8b42-a11562e79076_proyecto_pbip (4).zip.076\proyecto.pbip'.

Invocation Stack Trace:
   en Microsoft.Mashup.Host.Document.ExceptionExtensions.GetCurrentInvocationStackTrace()
   en Microsoft.Mashup.Client.UI.Shared.FeedbackErrorInfo..ctor(String message, Exception exception, Nullable`1 stackTraceInfo, String messageDetail)
   en Microsoft.PowerBI.Client.PowerBIUnexpectedExceptionHandler.HandleKnownExceptions(Exception e)
   en Microsoft.PowerBI.Client.PowerBIUnexpectedExceptionHandler.HandleException(Exception e)
   en Microsoft.PowerBI.Client.Windows.Utilities.PowerBIFormUnexpectedExceptionHandler.HandleException(Exception e)
   en Microsoft.PowerBI.Client.Windows.IExceptionHandlerExtensions.<HandleAwaitableAsyncExceptions>d__1.MoveNext()
   en System.Threading.ExecutionContext.RunInternal(ExecutionContext executionContext, ContextCallback callback, Object state, Boolean preserveSyncCtx)
   en System.Threading.ExecutionContext.Run(ExecutionContext executionContext, ContextCallback callback, Object state, Boolean preserveSyncCtx)
   en System.Runtime.CompilerServices.AsyncMethodBuilderCore.MoveNextRunner.Run()
   en System.Threading.Tasks.AwaitTaskContinuation.RunCallback(ContextCallback callback, Object state, Task& currentTask)
   en System.Threading.Tasks.Task.FinishContinuations()
   en System.Threading.Tasks.Task.Finish(Boolean bUserDelegateExecuted)
   en System.Threading.Tasks.Task`1.TrySetException(Object exceptionObject)
   en System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1.SetException(Exception exception)
   en Microsoft.PowerBI.Client.Windows.MainWindow.<<ActivateMainWindow>b__41_1>d.MoveNext()
   en System.Threading.ExecutionContext.RunInternal(ExecutionContext executionContext, ContextCallback callback, Object state, Boolean preserveSyncCtx)
   en System.Threading.ExecutionContext.Run(ExecutionContext executionContext, ContextCallback callback, Object state, Boolean preserveSyncCtx)
   en System.Runtime.CompilerServices.AsyncMethodBuilderCore.MoveNextRunner.Run()
   en System.Threading.Tasks.AwaitTaskContinuation.RunCallback(ContextCallback callback, Object state, Task& currentTask)
   en System.Threading.Tasks.Task.FinishContinuations()
   en System.Threading.Tasks.Task.Finish(Boolean bUserDelegateExecuted)
   en System.Threading.Tasks.Task`1.TrySetException(Object exceptionObject)
   en System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1.SetException(Exception exception)
   en Microsoft.PowerBI.Client.AppModule.<>c__DisplayClass4_2.<<Run>b__4>d.MoveNext()
   en System.Threading.ExecutionContext.RunInternal(ExecutionContext executionContext, ContextCallback callback, Object state, Boolean preserveSyncCtx)
   en System.Threading.ExecutionContext.Run(ExecutionContext executionContext, ContextCallback callback, Object state, Boolean preserveSyncCtx)
   en System.Runtime.CompilerServices.AsyncMethodBuilderCore.MoveNextRunner.Run()
   en System.Threading.Tasks.AwaitTaskContinuation.RunCallback(ContextCallback callback, Object state, Task& currentTask)
   en System.Threading.Tasks.Task.FinishContinuations()
   en System.Threading.Tasks.Task.Finish(Boolean bUserDelegateExecuted)
   en System.Threading.Tasks.Task`1.TrySetException(Object exceptionObject)
   en System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1.SetException(Exception exception)
   en Microsoft.PowerBI.Client.AppReportFlow.<ContinueLoadWithMainWindow>d__43.MoveNext()
   en System.Threading.ExecutionContext.RunInternal(ExecutionContext executionContext, ContextCallback callback, Object state, Boolean preserveSyncCtx)
   en System.Threading.ExecutionContext.Run(ExecutionContext executionContext, ContextCallback callback, Object state, Boolean preserveSyncCtx)
   en System.Runtime.CompilerServices.AsyncMethodBuilderCore.MoveNextRunner.Run()
   en System.Threading.Tasks.AwaitTaskContinuation.RunCallback(ContextCallback callback, Object state, Task& currentTask)
   en System.Threading.Tasks.Task.FinishContinuations()
   en System.Threading.Tasks.Task.Finish(Boolean bUserDelegateExecuted)
   en System.Threading.Tasks.Task`1.TrySetException(Object exceptionObject)
   en System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1.SetException(Exception exception)
   en Microsoft.PowerBI.Client.AppReportFlow.<OpenExistingReport>d__50.MoveNext()
   en System.Threading.ExecutionContext.RunInternal(ExecutionContext executionContext, ContextCallback callback, Object state, Boolean preserveSyncCtx)
   en System.Threading.ExecutionContext.Run(ExecutionContext executionContext, ContextCallback callback, Object state, Boolean preserveSyncCtx)
   en System.Runtime.CompilerServices.AsyncMethodBuilderCore.MoveNextRunner.Run()
   en System.Threading.Tasks.AwaitTaskContinuation.RunCallback(ContextCallback callback, Object state, Task& currentTask)
   en System.Threading.Tasks.Task.FinishContinuations()
   en System.Threading.Tasks.Task`1.TrySetResult(TResult result)
   en System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1.SetResult(TResult result)
   en System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1.SetResult(Task`1 completedTask)
   en Microsoft.PowerBI.Client.AppReportFlow.<EnsureEmptyDatabase>d__49.MoveNext()
   en System.Threading.ExecutionContext.RunInternal(ExecutionContext executionContext, ContextCallback callback, Object state, Boolean preserveSyncCtx)
   en System.Threading.ExecutionContext.Run(ExecutionContext executionContext, ContextCallback callback, Object state, Boolean preserveSyncCtx)
   en System.Runtime.CompilerServices.AsyncMethodBuilderCore.MoveNextRunner.Run()
   en System.Threading.Tasks.AwaitTaskContinuation.RunCallback(ContextCallback callback, Object state, Task& currentTask)
   en System.Threading.Tasks.Task.FinishContinuations()
   en System.Threading.Tasks.Task`1.TrySetResult(TResult result)
   en System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1.SetResult(TResult result)
   en System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1.SetResult(Task`1 completedTask)
   en Microsoft.PowerBI.Client.AppReportFlow.<CreateEmptyDatabase>d__48.MoveNext()
   en System.Threading.ExecutionContext.RunInternal(ExecutionContext executionContext, ContextCallback callback, Object state, Boolean preserveSyncCtx)
   en System.Threading.ExecutionContext.Run(ExecutionContext executionContext, ContextCallback callback, Object state, Boolean preserveSyncCtx)
   en System.Runtime.CompilerServices.AsyncMethodBuilderCore.MoveNextRunner.Run()
   en System.RuntimeMethodHandle.InvokeMethod(Object target, Object[] arguments, Signature sig, Boolean constructor)
   en System.Reflection.RuntimeMethodInfo.UnsafeInvokeInternal(Object obj, Object[] parameters, Object[] arguments)
   en System.Delegate.DynamicInvokeImpl(Object[] args)
   en System.Windows.Forms.Control.InvokeMarshaledCallbackDo(ThreadMethodEntry tme)
   en System.Windows.Forms.Control.InvokeMarshaledCallbackHelper(Object obj)
   en System.Threading.ExecutionContext.RunInternal(ExecutionContext executionContext, ContextCallback callback, Object state, Boolean preserveSyncCtx)
   en System.Threading.ExecutionContext.Run(ExecutionContext executionContext, ContextCallback callback, Object state, Boolean preserveSyncCtx)
   en System.Threading.ExecutionContext.Run(ExecutionContext executionContext, ContextCallback callback, Object state)
   en System.Windows.Forms.Control.InvokeMarshaledCallback(ThreadMethodEntry tme)
   en System.Windows.Forms.Control.InvokeMarshaledCallbacks()
   en System.Windows.Forms.Control.WndProc(Message& m)
   en System.Windows.Forms.NativeWindow.Callback(IntPtr hWnd, Int32 msg, IntPtr wparam, IntPtr lparam)
   en System.Windows.Forms.UnsafeNativeMethods.DispatchMessageW(MSG& msg)
   en System.Windows.Forms.UnsafeNativeMethods.DispatchMessageW(MSG& msg)
   en System.Windows.Forms.Application.ComponentManager.System.Windows.Forms.UnsafeNativeMethods.IMsoComponentManager.FPushMessageLoop(IntPtr dwComponentID, Int32 reason, Int32 pvLoopData)
   en System.Windows.Forms.Application.ThreadContext.RunMessageLoopInner(Int32 reason, ApplicationContext context)
   en System.Windows.Forms.Application.ThreadContext.RunMessageLoop(Int32 reason, ApplicationContext context)
   en System.Windows.Forms.Form.ShowDialog(IWin32Window owner)
   en Microsoft.Mashup.Client.UI.Shared.WindowManager.ShowModal[T](T dialog, Func`1 showModalFunction)
   en Microsoft.PowerBI.Client.AppModule.<>c__DisplayClass4_0.<Run>b__0()
   en Microsoft.PowerBI.Client.Windows.IExceptionHandlerExtensions.<>c__DisplayClass3_0.<HandleExceptionsWithNestedTasks>b__0()
   en Microsoft.Mashup.Host.Document.ExceptionHandlerExtensions.HandleExceptions(IExceptionHandler exceptionHandler, Action action)
   en Microsoft.PowerBI.Client.AppModule.Run()
   en Microsoft.PowerBI.Client.Program.RunApplicationFlow(String[] args, IPowerBIRootTrace trace)
   en Microsoft.PowerBI.Client.Program.Main(String[] args)


InnerException0.Stack Trace Message:
Expected 'artifacts' array containing 'report' artifact with valid 'path' property in 'C:\Users\Rafael\AppData\Local\Temp\27ec8b8d-f0b3-4965-8b42-a11562e79076_proyecto_pbip (4).zip.076\proyecto.pbip'.

InnerException0.Stack Trace:
   en Microsoft.PowerBI.Packaging.Project.PBIProjectShredder.<CallAndConvertIntoPathExceptionsAsync>d__32`1.MoveNext()
--- Fin del seguimiento de la pila de la ubicación anterior donde se produjo la excepción ---
   en System.Runtime.ExceptionServices.ExceptionDispatchInfo.Throw()
   en System.Runtime.CompilerServices.TaskAwaiter.HandleNonSuccessAndDebuggerNotification(Task task)
   en Microsoft.PowerBI.Packaging.Project.PBIProjectShredder.<GetUpgradedVariant>d__34`2.MoveNext()
--- Fin del seguimiento de la pila de la ubicación anterior donde se produjo la excepción ---
   en System.Runtime.ExceptionServices.ExceptionDispatchInfo.Throw()
   en System.Runtime.CompilerServices.TaskAwaiter.HandleNonSuccessAndDebuggerNotification(Task task)
   en Microsoft.PowerBI.Packaging.Project.PBIProjectShredder.<OpenProjectAsync>d__0.MoveNext()
--- Fin del seguimiento de la pila de la ubicación anterior donde se produjo la excepción ---
   en System.Runtime.ExceptionServices.ExceptionDispatchInfo.Throw()
   en System.Runtime.CompilerServices.TaskAwaiter.HandleNonSuccessAndDebuggerNotification(Task task)
   en Microsoft.PowerBI.Client.Windows.Services.BiProjectOperationHandler.<WithProjectExceptionConversion>d__51`1.MoveNext()

InnerException0.Invocation Stack Trace:
   en Microsoft.Mashup.Host.Document.ExceptionExtensions.GetCurrentInvocationStackTrace()
   en Microsoft.Mashup.Client.UI.Shared.FeedbackErrorInfo.GetFeedbackValuesFromException(Exception e, String prefix)
   en Microsoft.Mashup.Client.UI.Shared.FeedbackErrorInfo.GetFeedbackValuesFromInnerExceptions(Exception e, Int32 depth)
   en Microsoft.Mashup.Client.UI.Shared.FeedbackErrorInfo.CreateAdditionalErrorInfo(Exception e)
   en Microsoft.Mashup.Client.UI.Shared.FeedbackErrorInfo..ctor(String message, Exception exception, Nullable`1 stackTraceInfo, String messageDetail)
   en Microsoft.PowerBI.Client.PowerBIUnexpectedExceptionHandler.HandleKnownExceptions(Exception e)
   en Microsoft.PowerBI.Client.PowerBIUnexpectedExceptionHandler.HandleException(Exception e)
   en Microsoft.PowerBI.Client.Windows.Utilities.PowerBIFormUnexpectedExceptionHandler.HandleException(Exception e)
   en Microsoft.PowerBI.Client.Windows.IExceptionHandlerExtensions.<HandleAwaitableAsyncExceptions>d__1.MoveNext()
   en System.Threading.ExecutionContext.RunInternal(ExecutionContext executionContext, ContextCallback callback, Object state, Boolean preserveSyncCtx)
   en System.Threading.ExecutionContext.Run(ExecutionContext executionContext, ContextCallback callback, Object state, Boolean preserveSyncCtx)
   en System.Runtime.CompilerServices.AsyncMethodBuilderCore.MoveNextRunner.Run()
   en System.Threading.Tasks.AwaitTaskContinuation.RunCallback(ContextCallback callback, Object state, Task& currentTask)
   en System.Threading.Tasks.Task.FinishContinuations()
   en System.Threading.Tasks.Task.Finish(Boolean bUserDelegateExecuted)
   en System.Threading.Tasks.Task`1.TrySetException(Object exceptionObject)
   en System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1.SetException(Exception exception)
   en Microsoft.PowerBI.Client.Windows.MainWindow.<<ActivateMainWindow>b__41_1>d.MoveNext()
   en System.Threading.ExecutionContext.RunInternal(ExecutionContext executionContext, ContextCallback callback, Object state, Boolean preserveSyncCtx)
   en System.Threading.ExecutionContext.Run(ExecutionContext executionContext, ContextCallback callback, Object state, Boolean preserveSyncCtx)
   en System.Runtime.CompilerServices.AsyncMethodBuilderCore.MoveNextRunner.Run()
   en System.Threading.Tasks.AwaitTaskContinuation.RunCallback(ContextCallback callback, Object state, Task& currentTask)
   en System.Threading.Tasks.Task.FinishContinuations()
   en System.Threading.Tasks.Task.Finish(Boolean bUserDelegateExecuted)
   en System.Threading.Tasks.Task`1.TrySetException(Object exceptionObject)
   en System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1.SetException(Exception exception)
   en Microsoft.PowerBI.Client.AppModule.<>c__DisplayClass4_2.<<Run>b__4>d.MoveNext()
   en System.Threading.ExecutionContext.RunInternal(ExecutionContext executionContext, ContextCallback callback, Object state, Boolean preserveSyncCtx)
   en System.Threading.ExecutionContext.Run(ExecutionContext executionContext, ContextCallback callback, Object state, Boolean preserveSyncCtx)
   en System.Runtime.CompilerServices.AsyncMethodBuilderCore.MoveNextRunner.Run()
   en System.Threading.Tasks.AwaitTaskContinuation.RunCallback(ContextCallback callback, Object state, Task& currentTask)
   en System.Threading.Tasks.Task.FinishContinuations()
   en System.Threading.Tasks.Task.Finish(Boolean bUserDelegateExecuted)
   en System.Threading.Tasks.Task`1.TrySetException(Object exceptionObject)
   en System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1.SetException(Exception exception)
   en Microsoft.PowerBI.Client.AppReportFlow.<ContinueLoadWithMainWindow>d__43.MoveNext()
   en System.Threading.ExecutionContext.RunInternal(ExecutionContext executionContext, ContextCallback callback, Object state, Boolean preserveSyncCtx)
   en System.Threading.ExecutionContext.Run(ExecutionContext executionContext, ContextCallback callback, Object state, Boolean preserveSyncCtx)
   en System.Runtime.CompilerServices.AsyncMethodBuilderCore.MoveNextRunner.Run()
   en System.Threading.Tasks.AwaitTaskContinuation.RunCallback(ContextCallback callback, Object state, Task& currentTask)
   en System.Threading.Tasks.Task.FinishContinuations()
   en System.Threading.Tasks.Task.Finish(Boolean bUserDelegateExecuted)
   en System.Threading.Tasks.Task`1.TrySetException(Object exceptionObject)
   en System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1.SetException(Exception exception)
   en Microsoft.PowerBI.Client.AppReportFlow.<OpenExistingReport>d__50.MoveNext()
   en System.Threading.ExecutionContext.RunInternal(ExecutionContext executionContext, ContextCallback callback, Object state, Boolean preserveSyncCtx)
   en System.Threading.ExecutionContext.Run(ExecutionContext executionContext, ContextCallback callback, Object state, Boolean preserveSyncCtx)
   en System.Runtime.CompilerServices.AsyncMethodBuilderCore.MoveNextRunner.Run()
   en System.Threading.Tasks.AwaitTaskContinuation.RunCallback(ContextCallback callback, Object state, Task& currentTask)
   en System.Threading.Tasks.Task.FinishContinuations()
   en System.Threading.Tasks.Task`1.TrySetResult(TResult result)
   en System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1.SetResult(TResult result)
   en System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1.SetResult(Task`1 completedTask)
   en Microsoft.PowerBI.Client.AppReportFlow.<EnsureEmptyDatabase>d__49.MoveNext()
   en System.Threading.ExecutionContext.RunInternal(ExecutionContext executionContext, ContextCallback callback, Object state, Boolean preserveSyncCtx)
   en System.Threading.ExecutionContext.Run(ExecutionContext executionContext, ContextCallback callback, Object state, Boolean preserveSyncCtx)
   en System.Runtime.CompilerServices.AsyncMethodBuilderCore.MoveNextRunner.Run()
   en System.Threading.Tasks.AwaitTaskContinuation.RunCallback(ContextCallback callback, Object state, Task& currentTask)
   en System.Threading.Tasks.Task.FinishContinuations()
   en System.Threading.Tasks.Task`1.TrySetResult(TResult result)
   en System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1.SetResult(TResult result)
   en System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1.SetResult(Task`1 completedTask)
   en Microsoft.PowerBI.Client.AppReportFlow.<CreateEmptyDatabase>d__48.MoveNext()
   en System.Threading.ExecutionContext.RunInternal(ExecutionContext executionContext, ContextCallback callback, Object state, Boolean preserveSyncCtx)
   en System.Threading.ExecutionContext.Run(ExecutionContext executionContext, ContextCallback callback, Object state, Boolean preserveSyncCtx)
   en System.Runtime.CompilerServices.AsyncMethodBuilderCore.MoveNextRunner.Run()
   en System.RuntimeMethodHandle.InvokeMethod(Object target, Object[] arguments, Signature sig, Boolean constructor)
   en System.Reflection.RuntimeMethodInfo.UnsafeInvokeInternal(Object obj, Object[] parameters, Object[] arguments)
   en System.Delegate.DynamicInvokeImpl(Object[] args)
   en System.Windows.Forms.Control.InvokeMarshaledCallbackDo(ThreadMethodEntry tme)
   en System.Windows.Forms.Control.InvokeMarshaledCallbackHelper(Object obj)
   en System.Threading.ExecutionContext.RunInternal(ExecutionContext executionContext, ContextCallback callback, Object state, Boolean preserveSyncCtx)
   en System.Threading.ExecutionContext.Run(ExecutionContext executionContext, ContextCallback callback, Object state, Boolean preserveSyncCtx)
   en System.Threading.ExecutionContext.Run(ExecutionContext executionContext, ContextCallback callback, Object state)
   en System.Windows.Forms.Control.InvokeMarshaledCallback(ThreadMethodEntry tme)
   en System.Windows.Forms.Control.InvokeMarshaledCallbacks()
   en System.Windows.Forms.Control.WndProc(Message& m)
   en System.Windows.Forms.NativeWindow.Callback(IntPtr hWnd, Int32 msg, IntPtr wparam, IntPtr lparam)
   en System.Windows.Forms.UnsafeNativeMethods.DispatchMessageW(MSG& msg)
   en System.Windows.Forms.UnsafeNativeMethods.DispatchMessageW(MSG& msg)
   en System.Windows.Forms.Application.ComponentManager.System.Windows.Forms.UnsafeNativeMethods.IMsoComponentManager.FPushMessageLoop(IntPtr dwComponentID, Int32 reason, Int32 pvLoopData)
   en System.Windows.Forms.Application.ThreadContext.RunMessageLoopInner(Int32 reason, ApplicationContext context)
   en System.Windows.Forms.Application.ThreadContext.RunMessageLoop(Int32 reason, ApplicationContext context)
   en System.Windows.Forms.Form.ShowDialog(IWin32Window owner)
   en Microsoft.Mashup.Client.UI.Shared.WindowManager.ShowModal[T](T dialog, Func`1 showModalFunction)
   en Microsoft.PowerBI.Client.AppModule.<>c__DisplayClass4_0.<Run>b__0()
   en Microsoft.PowerBI.Client.Windows.IExceptionHandlerExtensions.<>c__DisplayClass3_0.<HandleExceptionsWithNestedTasks>b__0()
   en Microsoft.Mashup.Host.Document.ExceptionHandlerExtensions.HandleExceptions(IExceptionHandler exceptionHandler, Action action)
   en Microsoft.PowerBI.Client.AppModule.Run()
   en Microsoft.PowerBI.Client.Program.RunApplicationFlow(String[] args, IPowerBIRootTrace trace)
   en Microsoft.PowerBI.Client.Program.Main(String[] args)


InnerException1.Stack Trace Message:
Expected 'artifacts' array containing 'report' artifact with valid 'path' property in 'C:\Users\Rafael\AppData\Local\Temp\27ec8b8d-f0b3-4965-8b42-a11562e79076_proyecto_pbip (4).zip.076\proyecto.pbip'.

InnerException1.Stack Trace:
   en Microsoft.PowerBI.Packaging.Project.Artifacts.ArtifactShortcutBase.EnsureValid(String artifactName, String filePath)
   en Microsoft.PowerBI.Packaging.Project.PBIProjectSchemaValidator.ConstructV1WithJObjAdjustment[TV1](JObject jObj, String artifactName, String filePath, List`1 allWarnings)
   en Microsoft.PowerBI.Packaging.Project.PBIProjectSchemaValidator.FallbackConstructV1WithJObjAdjustment[TV1](JObject jObj, String artifactName, String filePath, List`1 allWarnings)
   en Microsoft.PowerBI.Packaging.Project.PBIProjectSchemaValidator.GetValidVariant[TV1,T](String json, String filePath)
   en Microsoft.PowerBI.Packaging.Project.PBIProjectShredder.<>c__DisplayClass34_0`2.<<GetUpgradedVariant>b__0>d.MoveNext()
--- Fin del seguimiento de la pila de la ubicación anterior donde se produjo la excepción ---
   en System.Runtime.ExceptionServices.ExceptionDispatchInfo.Throw()
   en System.Runtime.CompilerServices.TaskAwaiter.HandleNonSuccessAndDebuggerNotification(Task task)
   en Microsoft.PowerBI.Packaging.Project.PBIProjectShredder.<CallAndConvertIntoPathExceptionsAsync>d__32`1.MoveNext()

InnerException1.Invocation Stack Trace:
   en Microsoft.Mashup.Host.Document.ExceptionExtensions.GetCurrentInvocationStackTrace()
   en Microsoft.Mashup.Client.UI.Shared.FeedbackErrorInfo.GetFeedbackValuesFromException(Exception e, String prefix)
   en Microsoft.Mashup.Client.UI.Shared.FeedbackErrorInfo.GetFeedbackValuesFromInnerExceptions(Exception e, Int32 depth)
   en Microsoft.Mashup.Client.UI.Shared.FeedbackErrorInfo.GetFeedbackValuesFromInnerExceptions(Exception e, Int32 depth)
   en Microsoft.Mashup.Client.UI.Shared.FeedbackErrorInfo.CreateAdditionalErrorInfo(Exception e)
   en Microsoft.Mashup.Client.UI.Shared.FeedbackErrorInfo..ctor(String message, Exception exception, Nullable`1 stackTraceInfo, String messageDetail)
   en Microsoft.PowerBI.Client.PowerBIUnexpectedExceptionHandler.HandleKnownExceptions(Exception e)
   en Microsoft.PowerBI.Client.PowerBIUnexpectedExceptionHandler.HandleException(Exception e)
   en Microsoft.PowerBI.Client.Windows.Utilities.PowerBIFormUnexpectedExceptionHandler.HandleException(Exception e)
   en Microsoft.PowerBI.Client.Windows.IExceptionHandlerExtensions.<HandleAwaitableAsyncExceptions>d__1.MoveNext()
   en System.Threading.ExecutionContext.RunInternal(ExecutionContext executionContext, ContextCallback callback, Object state, Boolean preserveSyncCtx)
   en System.Threading.ExecutionContext.Run(ExecutionContext executionContext, ContextCallback callback, Object state, Boolean preserveSyncCtx)
   en System.Runtime.CompilerServices.AsyncMethodBuilderCore.MoveNextRunner.Run()
   en System.Threading.Tasks.AwaitTaskContinuation.RunCallback(ContextCallback callback, Object state, Task& currentTask)
   en System.Threading.Tasks.Task.FinishContinuations()
   en System.Threading.Tasks.Task.Finish(Boolean bUserDelegateExecuted)
   en System.Threading.Tasks.Task`1.TrySetException(Object exceptionObject)
   en System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1.SetException(Exception exception)
   en Microsoft.PowerBI.Client.Windows.MainWindow.<<ActivateMainWindow>b__41_1>d.MoveNext()
   en System.Threading.ExecutionContext.RunInternal(ExecutionContext executionContext, ContextCallback callback, Object state, Boolean preserveSyncCtx)
   en System.Threading.ExecutionContext.Run(ExecutionContext executionContext, ContextCallback callback, Object state, Boolean preserveSyncCtx)
   en System.Runtime.CompilerServices.AsyncMethodBuilderCore.MoveNextRunner.Run()
   en System.Threading.Tasks.AwaitTaskContinuation.RunCallback(ContextCallback callback, Object state, Task& currentTask)
   en System.Threading.Tasks.Task.FinishContinuations()
   en System.Threading.Tasks.Task.Finish(Boolean bUserDelegateExecuted)
   en System.Threading.Tasks.Task`1.TrySetException(Object exceptionObject)
   en System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1.SetException(Exception exception)
   en Microsoft.PowerBI.Client.AppModule.<>c__DisplayClass4_2.<<Run>b__4>d.MoveNext()
   en System.Threading.ExecutionContext.RunInternal(ExecutionContext executionContext, ContextCallback callback, Object state, Boolean preserveSyncCtx)
   en System.Threading.ExecutionContext.Run(ExecutionContext executionContext, ContextCallback callback, Object state, Boolean preserveSyncCtx)
   en System.Runtime.CompilerServices.AsyncMethodBuilderCore.MoveNextRunner.Run()
   en System.Threading.Tasks.AwaitTaskContinuation.RunCallback(ContextCallback callback, Object state, Task& currentTask)
   en System.Threading.Tasks.Task.FinishContinuations()
   en System.Threading.Tasks.Task.Finish(Boolean bUserDelegateExecuted)
   en System.Threading.Tasks.Task`1.TrySetException(Object exceptionObject)
   en System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1.SetException(Exception exception)
   en Microsoft.PowerBI.Client.AppReportFlow.<ContinueLoadWithMainWindow>d__43.MoveNext()
   en System.Threading.ExecutionContext.RunInternal(ExecutionContext executionContext, ContextCallback callback, Object state, Boolean preserveSyncCtx)
   en System.Threading.ExecutionContext.Run(ExecutionContext executionContext, ContextCallback callback, Object state, Boolean preserveSyncCtx)
   en System.Runtime.CompilerServices.AsyncMethodBuilderCore.MoveNextRunner.Run()
   en System.Threading.Tasks.AwaitTaskContinuation.RunCallback(ContextCallback callback, Object state, Task& currentTask)
   en System.Threading.Tasks.Task.FinishContinuations()
   en System.Threading.Tasks.Task.Finish(Boolean bUserDelegateExecuted)
   en System.Threading.Tasks.Task`1.TrySetException(Object exceptionObject)
   en System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1.SetException(Exception exception)
   en Microsoft.PowerBI.Client.AppReportFlow.<OpenExistingReport>d__50.MoveNext()
   en System.Threading.ExecutionContext.RunInternal(ExecutionContext executionContext, ContextCallback callback, Object state, Boolean preserveSyncCtx)
   en System.Threading.ExecutionContext.Run(ExecutionContext executionContext, ContextCallback callback, Object state, Boolean preserveSyncCtx)
   en System.Runtime.CompilerServices.AsyncMethodBuilderCore.MoveNextRunner.Run()
   en System.Threading.Tasks.AwaitTaskContinuation.RunCallback(ContextCallback callback, Object state, Task& currentTask)
   en System.Threading.Tasks.Task.FinishContinuations()
   en System.Threading.Tasks.Task`1.TrySetResult(TResult result)
   en System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1.SetResult(TResult result)
   en System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1.SetResult(Task`1 completedTask)
   en Microsoft.PowerBI.Client.AppReportFlow.<EnsureEmptyDatabase>d__49.MoveNext()
   en System.Threading.ExecutionContext.RunInternal(ExecutionContext executionContext, ContextCallback callback, Object state, Boolean preserveSyncCtx)
   en System.Threading.ExecutionContext.Run(ExecutionContext executionContext, ContextCallback callback, Object state, Boolean preserveSyncCtx)
   en System.Runtime.CompilerServices.AsyncMethodBuilderCore.MoveNextRunner.Run()
   en System.Threading.Tasks.AwaitTaskContinuation.RunCallback(ContextCallback callback, Object state, Task& currentTask)
   en System.Threading.Tasks.Task.FinishContinuations()
   en System.Threading.Tasks.Task`1.TrySetResult(TResult result)
   en System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1.SetResult(TResult result)
   en System.Runtime.CompilerServices.AsyncTaskMethodBuilder`1.SetResult(Task`1 completedTask)
   en Microsoft.PowerBI.Client.AppReportFlow.<CreateEmptyDatabase>d__48.MoveNext()
   en System.Threading.ExecutionContext.RunInternal(ExecutionContext executionContext, ContextCallback callback, Object state, Boolean preserveSyncCtx)
   en System.Threading.ExecutionContext.Run(ExecutionContext executionContext, ContextCallback callback, Object state, Boolean preserveSyncCtx)
   en System.Runtime.CompilerServices.AsyncMethodBuilderCore.MoveNextRunner.Run()
   en System.RuntimeMethodHandle.InvokeMethod(Object target, Object[] arguments, Signature sig, Boolean constructor)
   en System.Reflection.RuntimeMethodInfo.UnsafeInvokeInternal(Object obj, Object[] parameters, Object[] arguments)
   en System.Delegate.DynamicInvokeImpl(Object[] args)
   en System.Windows.Forms.Control.InvokeMarshaledCallbackDo(ThreadMethodEntry tme)
   en System.Windows.Forms.Control.InvokeMarshaledCallbackHelper(Object obj)
   en System.Threading.ExecutionContext.RunInternal(ExecutionContext executionContext, ContextCallback callback, Object state, Boolean preserveSyncCtx)
   en System.Threading.ExecutionContext.Run(ExecutionContext executionContext, ContextCallback callback, Object state, Boolean preserveSyncCtx)
   en System.Threading.ExecutionContext.Run(ExecutionContext executionContext, ContextCallback callback, Object state)
   en System.Windows.Forms.Control.InvokeMarshaledCallback(ThreadMethodEntry tme)
   en System.Windows.Forms.Control.InvokeMarshaledCallbacks()
   en System.Windows.Forms.Control.WndProc(Message& m)
   en System.Windows.Forms.NativeWindow.Callback(IntPtr hWnd, Int32 msg, IntPtr wparam, IntPtr lparam)
   en System.Windows.Forms.UnsafeNativeMethods.DispatchMessageW(MSG& msg)
   en System.Windows.Forms.UnsafeNativeMethods.DispatchMessageW(MSG& msg)
   en System.Windows.Forms.Application.ComponentManager.System.Windows.Forms.UnsafeNativeMethods.IMsoComponentManager.FPushMessageLoop(IntPtr dwComponentID, Int32 reason, Int32 pvLoopData)
   en System.Windows.Forms.Application.ThreadContext.RunMessageLoopInner(Int32 reason, ApplicationContext context)
   en System.Windows.Forms.Application.ThreadContext.RunMessageLoop(Int32 reason, ApplicationContext context)
   en System.Windows.Forms.Form.ShowDialog(IWin32Window owner)
   en Microsoft.Mashup.Client.UI.Shared.WindowManager.ShowModal[T](T dialog, Func`1 showModalFunction)
   en Microsoft.PowerBI.Client.AppModule.<>c__DisplayClass4_0.<Run>b__0()
   en Microsoft.PowerBI.Client.Windows.IExceptionHandlerExtensions.<>c__DisplayClass3_0.<HandleExceptionsWithNestedTasks>b__0()
   en Microsoft.Mashup.Host.Document.ExceptionHandlerExtensions.HandleExceptions(IExceptionHandler exceptionHandler, Action action)
   en Microsoft.PowerBI.Client.AppModule.Run()
   en Microsoft.PowerBI.Client.Program.RunApplicationFlow(String[] args, IPowerBIRootTrace trace)
   en Microsoft.PowerBI.Client.Program.Main(String[] args)


OS Version:
Microsoft Windows NT 10.0.26200.0 (x64 es-MX)

CLR Version:
4.8 or later [Release Number = 533509]

Peak Virtual Memory:
85.7 GB

Private Memory:
326 MB

Peak Working Set:
398 MB

IE Version:
11.1882.26100.0

User ID:
b05376d1-7cc7-4c78-8a13-d4603a53889d

Workbook Package Info:
1* - es-PE, Query Groups: 0, fastCombine: Disabled, runBackgroundAnalysis: False.

Telemetry Enabled:
True

Snapshot Trace Logs:
C:\Users\Rafael\AppData\Local\Microsoft\Power BI Desktop\FrownSnapShot44109eb5-6d53-4f10-9e4a-493c1128eef1.zip

Model Default Mode:
Empty

Model Version:
PowerBI_V3

Performance Trace Logs:
C:\Users\Rafael\AppData\Local\Microsoft\Power BI Desktop\PerformanceTraces.zip

Enabled Preview Features:
PBI_DatabricksAdbcVersionEnabled
PBI_googleBigQueryAdbcVersionEnabled
PBI_scorecardVisual
PBI_setLabelOnExportPdf
PBI_oneDriveSave
PBI_oneDriveShare
PBI_odspSaveBackgroundUpload
PBI_modernOfficeFilePicker
PBI_useModernPublishDialogs
PBI_gitIntegration
PBI_tmdlInDataset
PBI_enhancedReportFormat
PBI_advancedSlicerTypeList
PBI_aiNarrativesVisual
PBI_visualCalculationsAuthoring
PBI_copilotUnifiedTooling
PBI_UserInstalledNetezzaODBCDriver
PBI_sqlDbNativeArtifactsOnDesktop
PBI_enableExportQueries

Disabled Preview Features:
PBI_UseRedshiftODBCV2
PBI_snowflakeLegacyOdbcVersionEnabled
PBI_shapeMapVisualEnabled
PBI_SpanishLinguisticsEnabled
PBI_qnaLiveConnect
PBI_b2bExternalDatasetSharing
PBI_onObject
PBI_publishDialogsSupportSubfolders
PBI_enhancedReportFormatPBIX
PBI_qnaImproveLsdlCopilot
PBI_customCalendars
MashupFlight_EnableOracleBundledOdacProviderV2
PBI_supportUDFs
PBI_newVisualDefaults2026

Disabled DirectQuery Options:
TreatHanaAsRelationalSource

Cloud:
GlobalCloud

PowerBINonFatalError_ErrorCode:


InnerException0.PowerBINonFatalError_ErrorDescription:
ReportPathInvalid: Path: PBIP Shortcut

InnerException1.PowerBINonFatalError_ErrorDescription:
ReportPathInvalid: ArtifactName: ArtifactShortcutV1

DPI Scale:
125%

Supported Services:
Power BI

Formulas:


section Section1;

WebView2 Runtime Version:
147.0.3912.60

WebView2 SDK Version:
1.0.2365.46
