def findDecision(obj):
   # Feature: RSI, Instances: 115, Entropy: 0.9999
   if obj[1] == 'Hold':
      # Feature: MACD, Instances: 92, Entropy: 0.9945
      if obj[2] == 'Sell':
         # Feature: BB, Instances: 53, Entropy: 0.9562
         if obj[3] == 'Sell':
            # Feature: SMA2, Instances: 48, Entropy: 0.9377
            if obj[5] == 'Buy':
               # Feature: SMA1, Instances: 31, Entropy: 0.9812
               if obj[4] == 'Buy':
                  # Feature: Closing, Instances: 25, Entropy: 0.9988
                  if obj[0]<=77.0:
                     return 'Yes'
                  elif obj[0]>77.0:
                     return 'No'
                  else:
                     return 'No'
               elif obj[4] == 'Sell':
                  # Feature: Closing, Instances: 6, Entropy: 0.65
                  if obj[0]<=77.0:
                     return 'No'
                  else:
                     return 'No'
               else:
                  return 'No'
            elif obj[5] == 'Sell':
               # Feature: Closing, Instances: 17, Entropy: 0.7871
               if obj[0]<=77.0:
                  # Feature: SMA1, Instances: 15, Entropy: 0.8366
                  if obj[4] == 'Buy':
                     return 'No'
                  elif obj[4] == 'Sell':
                     return 'No'
                  else:
                     return 'No'
               elif obj[0]>77.0:
                  return 'No'
               else:
                  return 'No'
            else:
               return 'No'
         elif obj[3] == 'Hold':
            return 'Yes'
         elif obj[3] == 'Buy':
            return 'No'
         else:
            return 'No'
      elif obj[2] == 'Buy':
         # Feature: Closing, Instances: 39, Entropy: 0.9881
         if obj[0]<=77.0:
            # Feature: BB, Instances: 30, Entropy: 0.9968
            if obj[3] == 'Sell':
               # Feature: SMA2, Instances: 19, Entropy: 0.998
               if obj[5] == 'Sell':
                  # Feature: SMA1, Instances: 16, Entropy: 0.9887
                  if obj[4] == 'Sell':
                     return 'Yes'
                  elif obj[4] == 'Buy':
                     return 'No'
                  else:
                     return 'No'
               elif obj[5] == 'Buy':
                  # Feature: SMA1, Instances: 3, Entropy: 0.9183
                  if obj[4] == 'Sell':
                     return 'No'
                  else:
                     return 'No'
               else:
                  return 'No'
            elif obj[3] == 'Hold':
               # Feature: SMA1, Instances: 10, Entropy: 0.8813
               if obj[4] == 'Buy':
                  # Feature: SMA2, Instances: 6, Entropy: 0.65
                  if obj[5] == 'Buy':
                     return 'No'
                  elif obj[5] == 'Sell':
                     return 'No'
                  else:
                     return 'No'
               elif obj[4] == 'Sell':
                  # Feature: SMA2, Instances: 4, Entropy: 1.0
                  if obj[5] == 'Sell':
                     return 'Yes'
                  elif obj[5] == 'Buy':
                     return 'No'
                  else:
                     return 'No'
               else:
                  return 'No'
            elif obj[3] == 'Buy':
               return 'Yes'
            else:
               return 'Yes'
         elif obj[0]>77.0:
            # Feature: SMA1, Instances: 9, Entropy: 0.5033
            if obj[4] == 'Buy':
               return 'Yes'
            elif obj[4] == 'Sell':
               # Feature: BB, Instances: 3, Entropy: 0.9183
               if obj[3] == 'Sell':
                  # Feature: SMA2, Instances: 3, Entropy: 0.9183
                  if obj[5] == 'Sell':
                     return 'Yes'
                  else:
                     return 'Yes'
               else:
                  return 'Yes'
            else:
               return 'Yes'
         else:
            return 'Yes'
      else:
         return 'Yes'
   elif obj[1] == 'Sell':
      # Feature: SMA1, Instances: 18, Entropy: 0.65
      if obj[4] == 'Buy':
         # Feature: Closing, Instances: 14, Entropy: 0.3712
         if obj[0]>77.0:
            return 'Yes'
         elif obj[0]<=77.0:
            # Feature: MACD, Instances: 7, Entropy: 0.5917
            if obj[2] == 'Buy':
               # Feature: BB, Instances: 7, Entropy: 0.5917
               if obj[3] == 'Hold':
                  # Feature: SMA2, Instances: 7, Entropy: 0.5917
                  if obj[5] == 'Buy':
                     return 'Yes'
                  else:
                     return 'Yes'
               else:
                  return 'Yes'
            else:
               return 'Yes'
         else:
            return 'Yes'
      elif obj[4] == 'Sell':
         # Feature: SMA2, Instances: 4, Entropy: 1.0
         if obj[5] == 'Buy':
            # Feature: Closing, Instances: 3, Entropy: 0.9183
            if obj[0]<=77.0:
               # Feature: MACD, Instances: 3, Entropy: 0.9183
               if obj[2] == 'Buy':
                  # Feature: BB, Instances: 3, Entropy: 0.9183
                  if obj[3] == 'Hold':
                     return 'Yes'
                  else:
                     return 'Yes'
               else:
                  return 'Yes'
            else:
               return 'Yes'
         elif obj[5] == 'Sell':
            return 'No'
         else:
            return 'No'
      else:
         return 'No'
   elif obj[1] == 'Buy':
      return 'No'
   else:
      return 'No'
